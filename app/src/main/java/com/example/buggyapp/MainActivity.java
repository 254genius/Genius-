package com.example.buggyapp;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private EditText emailInput;
    private TextView resultText;
    private Button submitButton;
    private List<String> userEmails;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        emailInput = findViewById(R.id.email_input);
        resultText = findViewById(R.id.result_text);
        submitButton = findViewById(R.id.submit_button);
        userEmails = new ArrayList<>();
        
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                processEmail();
            }
        });
    }
    
    // BUG 1: Logic Error - Incorrect email validation
    private boolean isValidEmail(String email) {
        // This regex is too permissive and allows invalid emails
        return email.contains("@");
    }
    
    // FIXED: Removed static reference to prevent memory leak
    // Use instance variable or proper data persistence instead
    
    private void processEmail() {
        String email = emailInput.getText().toString();
        
        if (isValidEmail(email)) {
            userEmails.add(email);
            // FIXED: Only use instance variable to avoid memory leak
            
            // FIXED: Use parameterized query to prevent SQL injection
            String query = "SELECT * FROM users WHERE email = ?";
            resultText.setText("Query: " + query + " [Parameter: " + email + "]");
            
            // Simulate database operation with parameterized query
            executeParameterizedQuery(query, email);
        } else {
            resultText.setText("Invalid email format");
        }
    }
    
    private void executeParameterizedQuery(String query, String parameter) {
        // Simulated parameterized database query execution
        // In real app, use PreparedStatement with parameters
        System.out.println("Executing parameterized query: " + query);
        System.out.println("With parameter: " + parameter);
        
        // Example of how this would look with actual database code:
        // PreparedStatement stmt = connection.prepareStatement(query);
        // stmt.setString(1, parameter);
        // ResultSet rs = stmt.executeQuery();
    }
    
    // Additional method with potential null pointer exception
    private void processUserData(String data) {
        // BUG 4: Potential NullPointerException
        if (data.length() > 0) { // No null check
            System.out.println("Processing: " + data);
        }
    }
}