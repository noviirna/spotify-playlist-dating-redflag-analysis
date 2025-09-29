import unittest
from unittest.mock import Mock, patch, MagicMock
import sys
import os

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from noviirnawati.sdk.integration import build_prompt, ai_analysis
from noviirnawati.model.model import PlaylistItem


class TestIntegration(unittest.TestCase):
    """Test cases for integration functions"""
    
    def test_build_prompt_empty_list(self):
        """Test build_prompt with empty list"""
        result = build_prompt([])
        self.assertEqual(result, "")
    
    def test_build_prompt_single_item(self):
        """Test build_prompt with single item"""
        items = [PlaylistItem("Test Song", "Test Artist")]
        result = build_prompt(items)
        
        expected = "Playlist Data (Semicolon-separated list: Song Title - Artist; Song Title - Artist, ...): Test Song - Test Artist;"
        self.assertEqual(result, expected)
    
    def test_build_prompt_multiple_items(self):
        """Test build_prompt with multiple items"""
        items = [
            PlaylistItem("Song 1", "Artist 1"),
            PlaylistItem("Song 2", "Artist 2"),
            PlaylistItem("Song 3", "Artist 3")
        ]
        result = build_prompt(items)
        
        expected = "Playlist Data (Semicolon-separated list: Song Title - Artist; Song Title - Artist, ...): Song 1 - Artist 1; Song 2 - Artist 2; Song 3 - Artist 3;"
        self.assertEqual(result, expected)
    
    def test_build_prompt_with_special_characters(self):
        """Test build_prompt with special characters"""
        items = [PlaylistItem("Song with émojis 🎵", "Artist with ñ")]
        result = build_prompt(items)
        
        expected = "Playlist Data (Semicolon-separated list: Song Title - Artist; Song Title - Artist, ...): Song with émojis 🎵 - Artist with ñ;"
        self.assertEqual(result, expected)
    
    @patch('noviirnawati.sdk.integration.ai_analysis_google')
    @patch('noviirnawati.sdk.integration.AI_ANALYSIS_SAVED_AS_MARKDOWN', False)
    def test_ai_analysis_success(self, mock_ai_analysis):
        """Test successful AI analysis"""
        # Arrange
        mock_ai_analysis.return_value = "Test analysis result"
        items = [PlaylistItem("Test Song", "Test Artist")]
        
        # Act
        result = ai_analysis(items, "https://open.spotify.com/playlist/123")
        
        # Assert
        self.assertEqual(result, "Test analysis result")
        mock_ai_analysis.assert_called_once()
    
    @patch('noviirnawati.sdk.integration.ai_analysis_google')
    @patch('noviirnawati.sdk.integration.AI_ANALYSIS_SAVED_AS_MARKDOWN', False)
    def test_ai_analysis_empty_prompt(self, mock_ai_analysis):
        """Test AI analysis with empty prompt"""
        # Arrange
        items = []
        
        # Act & Assert
        with self.assertRaises(AssertionError) as context:
            ai_analysis(items, "https://open.spotify.com/playlist/123")
        
        self.assertIn("No prompt context", str(context.exception))
        mock_ai_analysis.assert_not_called()
    
    @patch('noviirnawati.sdk.integration.ai_analysis_google')
    @patch('noviirnawati.sdk.integration.AI_ANALYSIS_SAVED_AS_MARKDOWN', False)
    def test_ai_analysis_api_error(self, mock_ai_analysis):
        """Test AI analysis when API returns error"""
        # Arrange
        mock_ai_analysis.side_effect = Exception("API Error")
        items = [PlaylistItem("Test Song", "Test Artist")]
        
        # Act
        result = ai_analysis(items, "https://open.spotify.com/playlist/123")
        
        # Assert
        self.assertEqual(result, "No Result, please try again with a different URL")
        mock_ai_analysis.assert_called_once()


if __name__ == '__main__':
    unittest.main()
