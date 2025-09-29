import unittest
import json
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from noviirnawati.model.model import PlaylistItem


class TestPlaylistItem(unittest.TestCase):
    """Test cases for PlaylistItem model"""
    
    def test_init(self):
        """Test PlaylistItem initialization"""
        item = PlaylistItem("Test Song", "Test Artist")
        
        self.assertEqual(item.title, "Test Song")
        self.assertEqual(item.artist, "Test Artist")
    
    def test_to_dict(self):
        """Test PlaylistItem to_dict method"""
        item = PlaylistItem("Test Song", "Test Artist")
        result = item.to_dict()
        
        expected = {"title": "Test Song", "artist": "Test Artist"}
        self.assertEqual(result, expected)
    
    def test_to_json(self):
        """Test PlaylistItem to_json method"""
        item = PlaylistItem("Test Song", "Test Artist")
        result = item.to_json()
        
        # Parse the JSON to verify it's valid
        parsed = json.loads(result)
        self.assertEqual(parsed["title"], "Test Song")
        self.assertEqual(parsed["artist"], "Test Artist")
    
    def test_encode(self):
        """Test PlaylistItem encode method"""
        item = PlaylistItem("Test Song", "Test Artist")
        result = item.encode()
        
        expected = {"title": "Test Song", "artist": "Test Artist"}
        self.assertEqual(result, expected)
    
    def test_with_special_characters(self):
        """Test PlaylistItem with special characters"""
        item = PlaylistItem("Song with émojis 🎵", "Artist with ñ")
        
        self.assertEqual(item.title, "Song with émojis 🎵")
        self.assertEqual(item.artist, "Artist with ñ")
        
        # Test JSON serialization with special characters
        json_result = item.to_json()
        parsed = json.loads(json_result)
        self.assertEqual(parsed["title"], "Song with émojis 🎵")
        self.assertEqual(parsed["artist"], "Artist with ñ")
    
    def test_with_empty_strings(self):
        """Test PlaylistItem with empty strings"""
        item = PlaylistItem("", "")
        
        self.assertEqual(item.title, "")
        self.assertEqual(item.artist, "")
        
        result = item.to_dict()
        self.assertEqual(result, {"title": "", "artist": ""})


if __name__ == '__main__':
    unittest.main()
