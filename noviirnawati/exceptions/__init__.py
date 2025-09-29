"""Custom exceptions for the Spotify Playlist Dating Red Flag Analysis project."""

from .spotify_exceptions import (
    SpotifyAPIError,
    SpotifyAuthenticationError,
    SpotifyPlaylistNotFoundError,
    SpotifyRateLimitError,
    SpotifyInvalidURLError
)

from .ai_exceptions import (
    AIAnalysisError,
    AIConfigurationError,
    AIServiceUnavailableError
)

from .validation_exceptions import (
    ValidationError,
    InvalidPlaylistURLError,
    EmptyPlaylistError
)

__all__ = [
    'SpotifyAPIError',
    'SpotifyAuthenticationError', 
    'SpotifyPlaylistNotFoundError',
    'SpotifyRateLimitError',
    'SpotifyInvalidURLError',
    'AIAnalysisError',
    'AIConfigurationError',
    'AIServiceUnavailableError',
    'ValidationError',
    'InvalidPlaylistURLError',
    'EmptyPlaylistError'
]
