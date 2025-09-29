import unittest
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from noviirnawati.helper.validator import validate_url, str_is_empty_or_none, dct_is_empty_or_none


class TestValidator(unittest.TestCase):
    """Test cases for validator functions"""
    
    def test_validate_url_valid(self):
        """Test URL validation with valid URLs"""
        valid_urls = [
            'https://open.spotify.com/playlist/1234567890',
            'http://example.com',
            'https://www.google.com',
            'https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq'
        ]
        
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(validate_url(url))
    
    def test_validate_url_invalid(self):
        """Test URL validation with invalid URLs"""
        invalid_urls = [
            'not_a_url',
            'ftp://invalid',
            'spotify.com/playlist/123',
            '',
            None
        ]
        
        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(validate_url(url))
    
    def test_str_is_empty_or_none(self):
        """Test string empty or None validation"""
        # Empty strings
        self.assertTrue(str_is_empty_or_none(""))
        self.assertTrue(str_is_empty_or_none(None))
        
        # Non-empty strings
        self.assertFalse(str_is_empty_or_none("hello"))
        self.assertFalse(str_is_empty_or_none(" "))
        self.assertFalse(str_is_empty_or_none("0"))
    
    def test_dct_is_empty_or_none(self):
        """Test dictionary empty or None validation"""
        # Empty or None dictionaries
        self.assertTrue(dct_is_empty_or_none({}))
        self.assertTrue(dct_is_empty_or_none(None))
        
        # Non-empty dictionaries
        self.assertFalse(dct_is_empty_or_none({"key": "value"}))
        self.assertFalse(dct_is_empty_or_none({"key": None}))


if __name__ == '__main__':
    unittest.main()
