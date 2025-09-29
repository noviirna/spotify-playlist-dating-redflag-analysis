import unittest
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from noviirnawati.helper.str_utility import extract_playlist_id


class TestStrUtility(unittest.TestCase):
    """Test cases for string utility functions"""
    
    def test_extract_playlist_id_valid(self):
        """Test playlist ID extraction with valid URLs"""
        test_cases = [
            ("https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq", "7wARwuyCiPRMURGmh6xTLq"),
            ("https://open.spotify.com/playlist/1234567890", "1234567890"),
            ("https://open.spotify.com/playlist/abc123def456", "abc123def456"),
            ("https://open.spotify.com/playlist/7wARwuyCiPRMURGmh6xTLq?si=something", "7wARwuyCiPRMURGmh6xTLq"),
        ]
        
        for url, expected_id in test_cases:
            with self.subTest(url=url):
                result = extract_playlist_id(url)
                self.assertEqual(result, expected_id)
    
    def test_extract_playlist_id_invalid(self):
        """Test playlist ID extraction with invalid URLs"""
        invalid_urls = [
            "https://open.spotify.com/album/1234567890",
            "https://open.spotify.com/track/1234567890",
            "https://open.spotify.com/artist/1234567890",
            "https://example.com/playlist/1234567890",
            "not_a_url",
            "",
            None
        ]
        
        for url in invalid_urls:
            with self.subTest(url=url):
                result = extract_playlist_id(url)
                self.assertEqual(result, "")
    
    def test_extract_playlist_id_edge_cases(self):
        """Test playlist ID extraction with edge cases"""
        test_cases = [
            ("https://open.spotify.com/playlist/", ""),
            ("https://open.spotify.com/playlist/123", "123"),
            ("https://open.spotify.com/playlist/123/extra", "123"),
        ]
        
        for url, expected_id in test_cases:
            with self.subTest(url=url):
                result = extract_playlist_id(url)
                self.assertEqual(result, expected_id)


if __name__ == '__main__':
    unittest.main()
