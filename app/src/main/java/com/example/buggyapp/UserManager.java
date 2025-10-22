package com.example.buggyapp;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class UserManager {
    private Map<String, String> userCredentials;
    private static UserManager instance;
    
    // FIXED: Thread-safe singleton using double-checked locking
    public static UserManager getInstance() {
        if (instance == null) {
            synchronized (UserManager.class) {
                if (instance == null) {
                    instance = new UserManager();
                }
            }
        }
        return instance;
    }
    
    private UserManager() {
        userCredentials = new ConcurrentHashMap<>(); // Thread-safe
    }
    
    // BUG 6: Security vulnerability - storing passwords in plain text
    public void addUser(String username, String password) {
        userCredentials.put(username, password); // Plain text password storage
    }
    
    public boolean authenticateUser(String username, String password) {
        String storedPassword = userCredentials.get(username);
        return password.equals(storedPassword); // Plain text comparison
    }
    
    // BUG 7: Resource leak - missing close operation
    public void processLargeFile(String filename) {
        try {
            java.io.FileInputStream fis = new java.io.FileInputStream(filename);
            // Process file but never close the stream
            byte[] buffer = new byte[1024];
            fis.read(buffer);
            // Missing fis.close() - resource leak
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}