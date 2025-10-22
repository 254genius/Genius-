"""
Utility functions for the application
"""

def validate_password(password):
    """
    Validate password strength
    Requirements: At least 8 characters, contains uppercase, lowercase, and digit
    """
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    return has_upper and has_lower and has_digit

def get_substring(text, start, end):
    """
    Get a substring from text between start and end indices (inclusive)
    """
    # Fixed: Added +1 to end index to make it inclusive
    return text[start:end+1]

def chunk_list(items, chunk_size):
    """
    Split a list into chunks of specified size
    """
    chunks = []
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i:i + chunk_size])
    return chunks

def is_valid_email(email):
    """Basic email validation"""
    if not email or '@' not in email:
        return False
    
    parts = email.split('@')
    if len(parts) != 2:
        return False
    
    username, domain = parts
    if not username or not domain:
        return False
    
    if '.' not in domain:
        return False
    
    return True
