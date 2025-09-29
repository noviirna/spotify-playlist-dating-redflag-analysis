"""AI service specific exceptions."""


class AIAnalysisError(Exception):
    """Base exception for AI analysis related errors."""
    
    def __init__(self, message: str, error_code: str = None, details: dict = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}


class AIConfigurationError(AIAnalysisError):
    """Raised when AI service configuration is invalid."""
    
    def __init__(self, message: str = "AI service configuration is invalid"):
        super().__init__(message, error_code="CONFIG_ERROR")


class AIServiceUnavailableError(AIAnalysisError):
    """Raised when AI service is unavailable."""
    
    def __init__(self, message: str = "AI service is currently unavailable", retry_after: int = None):
        super().__init__(message, error_code="SERVICE_UNAVAILABLE")
        self.retry_after = retry_after


class AIContentGenerationError(AIAnalysisError):
    """Raised when AI content generation fails."""
    
    def __init__(self, message: str = "Failed to generate AI content"):
        super().__init__(message, error_code="GENERATION_ERROR")


class AISafetyFilterError(AIAnalysisError):
    """Raised when content is blocked by AI safety filters."""
    
    def __init__(self, message: str = "Content blocked by safety filters"):
        super().__init__(message, error_code="SAFETY_FILTER")
