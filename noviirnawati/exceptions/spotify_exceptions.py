"""Spotify API specific exceptions."""


class SpotifyAPIError(Exception):
    """Base exception for Spotify API related errors."""
    
    def __init__(self, message: str, status_code: int = None, response_data: dict = None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}


class SpotifyAuthenticationError(SpotifyAPIError):
    """Raised when Spotify API authentication fails."""
    
    def __init__(self, message: str = "Spotify API authentication failed"):
        super().__init__(message, status_code=401)


class SpotifyPlaylistNotFoundError(SpotifyAPIError):
    """Raised when a playlist is not found or not accessible."""
    
    def __init__(self, playlist_id: str, message: str = None):
        if message is None:
            message = f"Playlist '{playlist_id}' not found or not accessible"
        super().__init__(message, status_code=404)
        self.playlist_id = playlist_id


class SpotifyRateLimitError(SpotifyAPIError):
    """Raised when Spotify API rate limit is exceeded."""
    
    def __init__(self, message: str = "Spotify API rate limit exceeded", retry_after: int = None):
        super().__init__(message, status_code=429)
        self.retry_after = retry_after


class SpotifyInvalidURLError(SpotifyAPIError):
    """Raised when an invalid Spotify URL is provided."""
    
    def __init__(self, url: str, message: str = None):
        if message is None:
            message = f"Invalid Spotify URL: {url}"
        super().__init__(message, status_code=400)
        self.url = url
