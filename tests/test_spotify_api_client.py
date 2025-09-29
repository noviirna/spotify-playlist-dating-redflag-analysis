import unittest
from unittest.mock import Mock, patch, MagicMock
import os
import sys

# Add the parent directory to the path to import the modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from noviirnawati.spotify.api_client import SpotifyAPIClient
from noviirnawati.model.model import PlaylistItem


class TestSpotifyAPIClient(unittest.TestCase):
    """Test cases for SpotifyAPIClient"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Mock environment variables
        self.mock_env = {
            'SPOTIFY_CLIENT_ID': 'test_client_id',
            'SPOTIFY_CLIENT_SECRET': 'test_client_secret'
        }
    
    @patch.dict(os.environ, {'SPOTIFY_CLIENT_ID': 'test_client_id', 'SPOTIFY_CLIENT_SECRET': 'test_client_secret'})
    @patch('noviirnawati.spotify.api_client.spotipy.Spotify')
    @patch('noviirnawati.spotify.api_client.SpotifyClientCredentials')
    def test_init_success(self, mock_credentials, mock_spotify):
        """Test successful initialization of SpotifyAPIClient"""
        # Arrange
        mock_credentials.return_value = Mock()
        mock_spotify.return_value = Mock()
        
        # Act
        client = SpotifyAPIClient()
        
        # Assert
        self.assertIsNotNone(client)
        mock_credentials.assert_called_once_with(
            client_id='test_client_id',
            client_secret='test_client_secret'
        )
        mock_spotify.assert_called_once()
    
    @patch.dict(os.environ, {}, clear=True)
    def test_init_missing_credentials(self):
        """Test initialization fails when credentials are missing"""
        # Act & Assert
        with self.assertRaises(Exception) as context:
            SpotifyAPIClient()
        
        self.assertIn("SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET", str(context.exception))
    
    @patch.dict(os.environ, {'SPOTIFY_CLIENT_ID': 'test_client_id', 'SPOTIFY_CLIENT_SECRET': 'test_client_secret'})
    @patch('noviirnawati.spotify.api_client.spotipy.Spotify')
    @patch('noviirnawati.spotify.api_client.SpotifyClientCredentials')
    def test_get_playlist_tracks_success(self, mock_credentials, mock_spotify):
        """Test successful playlist tracks retrieval"""
        # Arrange
        mock_spotify_instance = Mock()
        mock_spotify.return_value = mock_spotify_instance
        
        # Mock playlist tracks response
        mock_tracks_response = {
            'items': [
                {
                    'track': {
                        'name': 'Test Song 1',
                        'artists': [{'name': 'Artist 1'}, {'name': 'Artist 2'}]
                    }
                },
                {
                    'track': {
                        'name': 'Test Song 2',
                        'artists': [{'name': 'Artist 3'}]
                    }
                }
            ],
            'next': None
        }
        mock_spotify_instance.playlist_tracks.return_value = mock_tracks_response
        
        client = SpotifyAPIClient()
        
        # Act
        result = client.get_playlist_tracks('https://open.spotify.com/playlist/1234567890')
        
        # Assert
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], PlaylistItem)
        self.assertEqual(result[0].title, 'Test Song 1')
        self.assertEqual(result[0].artist, 'Artist 1, Artist 2')
        self.assertEqual(result[1].title, 'Test Song 2')
        self.assertEqual(result[1].artist, 'Artist 3')
    
    @patch.dict(os.environ, {'SPOTIFY_CLIENT_ID': 'test_client_id', 'SPOTIFY_CLIENT_SECRET': 'test_client_secret'})
    @patch('noviirnawati.spotify.api_client.spotipy.Spotify')
    @patch('noviirnawati.spotify.api_client.SpotifyClientCredentials')
    def test_get_playlist_tracks_invalid_url(self, mock_credentials, mock_spotify):
        """Test playlist tracks retrieval with invalid URL"""
        # Arrange
        mock_spotify_instance = Mock()
        mock_spotify.return_value = mock_spotify_instance
        
        client = SpotifyAPIClient()
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            client.get_playlist_tracks('invalid_url')
        
        self.assertIn("Invalid playlist URL", str(context.exception))
    
    @patch.dict(os.environ, {'SPOTIFY_CLIENT_ID': 'test_client_id', 'SPOTIFY_CLIENT_SECRET': 'test_client_secret'})
    @patch('noviirnawati.spotify.api_client.spotipy.Spotify')
    @patch('noviirnawati.spotify.api_client.SpotifyClientCredentials')
    def test_get_playlist_tracks_api_error(self, mock_credentials, mock_spotify):
        """Test playlist tracks retrieval when API returns error"""
        # Arrange
        mock_spotify_instance = Mock()
        mock_spotify.return_value = mock_spotify_instance
        mock_spotify_instance.playlist_tracks.side_effect = Exception("API Error")
        
        client = SpotifyAPIClient()
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            client.get_playlist_tracks('https://open.spotify.com/playlist/1234567890')
        
        self.assertIn("Unexpected error", str(context.exception))
    
    @patch.dict(os.environ, {'SPOTIFY_CLIENT_ID': 'test_client_id', 'SPOTIFY_CLIENT_SECRET': 'test_client_secret'})
    @patch('noviirnawati.spotify.api_client.spotipy.Spotify')
    @patch('noviirnawati.spotify.api_client.SpotifyClientCredentials')
    def test_get_playlist_info_success(self, mock_credentials, mock_spotify):
        """Test successful playlist info retrieval"""
        # Arrange
        mock_spotify_instance = Mock()
        mock_spotify.return_value = mock_spotify_instance
        
        # Mock playlist response
        mock_playlist_response = {
            'name': 'Test Playlist',
            'description': 'A test playlist',
            'owner': {'display_name': 'Test User'},
            'tracks': {'total': 10},
            'public': True
        }
        mock_spotify_instance.playlist.return_value = mock_playlist_response
        
        client = SpotifyAPIClient()
        
        # Act
        result = client.get_playlist_info('https://open.spotify.com/playlist/1234567890')
        
        # Assert
        self.assertEqual(result['name'], 'Test Playlist')
        self.assertEqual(result['description'], 'A test playlist')
        self.assertEqual(result['owner'], 'Test User')
        self.assertEqual(result['total_tracks'], 10)
        self.assertTrue(result['public'])


if __name__ == '__main__':
    unittest.main()
