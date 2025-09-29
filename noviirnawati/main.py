# load .env file in /env directory
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv('./env/.env', usecwd=False))

import sys
import logging
from .helper import validator
from .spotify.api_client import SpotifyAPIClient
from .sdk.integration import ai_analysis
from .exceptions import (
    SpotifyAPIError,
    SpotifyAuthenticationError,
    SpotifyPlaylistNotFoundError,
    SpotifyRateLimitError,
    InvalidPlaylistURLError,
    EmptyPlaylistError,
    AIAnalysisError
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m noviirnawati.main <spotify_playlist_url>")
        sys.exit(1)
    
    playlist_link = sys.argv[1]
    
    if validator.str_is_empty_or_none(playlist_link):
        print("Playlist link is empty. Please enter a valid playlist link.")
        sys.exit(1)
    
    try:
        # Initialize Spotify API client
        spotify_client = SpotifyAPIClient()
        
        # Get playlist tracks
        logger.info(f"Fetching tracks from playlist: {playlist_link}")
        songs_collection = spotify_client.get_playlist_tracks(playlist_link)
        
        # Perform AI analysis
        ai_analysis(songs_collection, playlist_link)
        
    except InvalidPlaylistURLError as e:
        logger.error(f"Invalid playlist URL: {str(e)}")
        print(f"Error: Invalid playlist URL. Please provide a valid Spotify playlist URL.")
        sys.exit(1)
    except SpotifyAuthenticationError as e:
        logger.error(f"Spotify authentication error: {str(e)}")
        print(f"Error: Spotify authentication failed. Please check your SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET.")
        sys.exit(1)
    except SpotifyPlaylistNotFoundError as e:
        logger.error(f"Playlist not found: {str(e)}")
        print(f"Error: Playlist not found or not accessible. Please check the playlist URL and ensure it's public.")
        sys.exit(1)
    except SpotifyRateLimitError as e:
        logger.error(f"Spotify rate limit exceeded: {str(e)}")
        print(f"Error: Spotify API rate limit exceeded. Please try again later.")
        sys.exit(1)
    except EmptyPlaylistError as e:
        logger.error(f"Empty playlist: {str(e)}")
        print(f"Error: The playlist is empty or has no accessible tracks.")
        sys.exit(1)
    except SpotifyAPIError as e:
        logger.error(f"Spotify API error: {str(e)}")
        print(f"Error: Spotify API error - {str(e)}")
        sys.exit(1)
    except AIAnalysisError as e:
        logger.error(f"AI analysis error: {str(e)}")
        print(f"Error: AI analysis failed - {str(e)}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error processing playlist: {str(e)}")
        print(f"Error: An unexpected error occurred - {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
