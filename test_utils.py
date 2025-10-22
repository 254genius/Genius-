"""
Unit tests for utility functions
"""
import unittest
from utils import validate_password, get_substring, chunk_list, is_valid_email

class TestUtils(unittest.TestCase):
    
    def test_validate_password(self):
        """Test password validation"""
        self.assertTrue(validate_password("Password123"))
        self.assertFalse(validate_password("pass"))
        self.assertFalse(validate_password("password"))
        self.assertFalse(validate_password("PASSWORD123"))
        
    def test_get_substring(self):
        """Test substring extraction"""
        text = "Hello World"
        # Should get "Hello" (indices 0-4 inclusive)
        result = get_substring(text, 0, 4)
        self.assertEqual(result, "Hello")  # This will fail due to the bug
        
        # Should get "World" (indices 6-10 inclusive)
        result = get_substring(text, 6, 10)
        self.assertEqual(result, "World")  # This will fail due to the bug
    
    def test_chunk_list(self):
        """Test list chunking"""
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        chunks = chunk_list(items, 3)
        self.assertEqual(chunks, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        
    def test_is_valid_email(self):
        """Test email validation"""
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertFalse(is_valid_email("invalid"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("user@"))

if __name__ == '__main__':
    unittest.main()
