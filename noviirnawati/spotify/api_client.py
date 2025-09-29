import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException
from typing import List, Optional
import logging

from ..model.model import PlaylistItem
from ..helper.validator import str_is_empty_or_none
from ..helper import str_utility
from ..exceptions import (
    SpotifyAPIError,
    SpotifyAuthenticationError,
    SpotifyPlaylistNotFoundError,
    SpotifyRateLimitError,
    SpotifyInvalidURLError,
    InvalidPlaylistURLError,
    EmptyPlaylistError
)

logger = logging.getLogger(__name__)


class SpotifyAPIClient:
    """Client for interacting with Spotify Web API"""
    
    def __init__(self):
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        
        if str_is_empty_or_none(self.client_id) or str_is_empty_or_none(self.client_secret):
            raise SpotifyAuthenticationError("SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET environment variables are required")
        
        try:
            # Initialize Spotify client with client credentials flow
            client_credentials_manager = SpotifyClientCredentials(
                client_id=self.client_id,
                client_secret=self.client_secret
            )
            self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        except Exception as e:
            logger.error(f"Failed to initialize Spotify client: {str(e)}")
            raise SpotifyAuthenticationError(f"Failed to initialize Spotify client: {str(e)}")
    
    def get_playlist_tracks(self, playlist_url: str) -> List[PlaylistItem]:
        """
        Fetch playlist tracks using Spotify Web API
        
        Args:
            playlist_url: Spotify playlist URL
            
        Returns:
            List of PlaylistItem objects containing track information
            
        Raises:
            InvalidPlaylistURLError: If playlist URL is invalid
            SpotifyPlaylistNotFoundError: If playlist is not found
            SpotifyRateLimitError: If rate limit is exceeded
            SpotifyAPIError: If API request fails
        """
        try:
            # Extract playlist ID from URL
            playlist_id = str_utility.extract_playlist_id(playlist_url)
            if str_is_empty_or_none(playlist_id):
                raise InvalidPlaylistURLError(playlist_url)
            
            logger.info(f"Fetching playlist tracks for ID: {playlist_id}")
            
            # Get playlist tracks
            results = self.sp.playlist_tracks(playlist_id)
            
            tracks = []
            while results:
                for item in results['items']:
                    if item['track'] is not None:  # Skip None tracks
                        track = item['track']
                        title = track.get('name', 'Unknown Title')
                        
                        # Get artist names
                        artists = track.get('artists', [])
                        artist_names = ', '.join([artist.get('name', 'Unknown Artist') for artist in artists])
                        
                        tracks.append(PlaylistItem(title, artist_names))
                
                # Check if there are more pages
                if results['next']:
                    results = self.sp.next(results)
                else:
                    break
            
            if not tracks:
                raise EmptyPlaylistError(playlist_id)
            
            logger.info(f"Successfully fetched {len(tracks)} tracks from playlist")
            return tracks
            
        except SpotifyException as e:
            logger.error(f"Spotify API error: {str(e)}")
            if e.http_status == 401:
                raise SpotifyAuthenticationError("Invalid Spotify credentials")
            elif e.http_status == 404:
                raise SpotifyPlaylistNotFoundError(playlist_id)
            elif e.http_status == 429:
                raise SpotifyRateLimitError("Rate limit exceeded")
            else:
                raise SpotifyAPIError(f"Spotify API error: {str(e)}", status_code=e.http_status)
        except (InvalidPlaylistURLError, EmptyPlaylistError):
            # Re-raise our custom exceptions
            raise
        except Exception as e:
            logger.error(f"Unexpected error fetching playlist tracks: {str(e)}")
            raise SpotifyAPIError(f"Unexpected error: {str(e)}")
    
    def get_playlist_info(self, playlist_url: str) -> dict:
        """
        Get basic playlist information
        
        Args:
            playlist_url: Spotify playlist URL
            
        Returns:
            Dictionary with playlist information
            
        Raises:
            InvalidPlaylistURLError: If playlist URL is invalid
            SpotifyPlaylistNotFoundError: If playlist is not found
            SpotifyAPIError: If API request fails
        """
        try:
            playlist_id = str_utility.extract_playlist_id(playlist_url)
            if str_is_empty_or_none(playlist_id):
                raise InvalidPlaylistURLError(playlist_url)
            
            playlist = self.sp.playlist(playlist_id)
            return {
                'name': playlist.get('name', 'Unknown Playlist'),
                'description': playlist.get('description', ''),
                'owner': playlist.get('owner', {}).get('display_name', 'Unknown'),
                'total_tracks': playlist.get('tracks', {}).get('total', 0),
                'public': playlist.get('public', False)
            }
            
        except SpotifyException as e:
            logger.error(f"Spotify API error fetching playlist info: {str(e)}")
            if e.http_status == 401:
                raise SpotifyAuthenticationError("Invalid Spotify credentials")
            elif e.http_status == 404:
                raise SpotifyPlaylistNotFoundError(playlist_id)
            elif e.http_status == 429:
                raise SpotifyRateLimitError("Rate limit exceeded")
            else:
                raise SpotifyAPIError(f"Spotify API error: {str(e)}", status_code=e.http_status)
        except InvalidPlaylistURLError:
            # Re-raise our custom exceptions
            raise
        except Exception as e:
            logger.error(f"Unexpected error fetching playlist info: {str(e)}")
            raise SpotifyAPIError(f"Unexpected error: {str(e)}")
