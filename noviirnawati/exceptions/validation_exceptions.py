"""Validation specific exceptions."""


class ValidationError(Exception):
    """Base exception for validation errors."""
    
    def __init__(self, message: str, field: str = None, value: str = None):
        super().__init__(message)
        self.message = message
        self.field = field
        self.value = value


class InvalidPlaylistURLError(ValidationError):
    """Raised when an invalid playlist URL is provided."""
    
    def __init__(self, url: str, message: str = None):
        if message is None:
            message = f"Invalid playlist URL: {url}"
        super().__init__(message, field="playlist_url", value=url)
        self.url = url


class EmptyPlaylistError(ValidationError):
    """Raised when a playlist is empty or has no tracks."""
    
    def __init__(self, playlist_id: str, message: str = None):
        if message is None:
            message = f"Playlist '{playlist_id}' is empty or has no accessible tracks"
        super().__init__(message, field="playlist_tracks", value=playlist_id)
        self.playlist_id = playlist_id


class InvalidConfigurationError(ValidationError):
    """Raised when application configuration is invalid."""
    
    def __init__(self, config_field: str, message: str = None):
        if message is None:
            message = f"Invalid configuration for field: {config_field}"
        super().__init__(message, field=config_field)
        self.config_field = config_field
