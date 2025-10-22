"""
Simple Flask web application with user authentication
"""
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            email TEXT,
            is_admin INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint - Fixed SQL injection vulnerability"""
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Fixed: Using parameterized queries to prevent SQL injection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return jsonify({
            'success': True,
            'user_id': user[0],
            'username': user[1],
            'is_admin': user[4]
        })
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, password, email)
        )
        conn.commit()
        return jsonify({'success': True, 'message': 'User registered successfully'})
    except sqlite3.IntegrityError:
        return jsonify({'success': False, 'message': 'Username already exists'}), 400
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
