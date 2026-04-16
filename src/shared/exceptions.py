"""Custom exception hierarchy for the Review Management Platform."""

from __future__ import annotations


class PlatformError(Exception):
    """Base exception for all platform errors."""

    def __init__(
        self,
        message: str,
        error_code: str = "PLATFORM_ERROR",
        status_code: int = 500,
        details: list[dict[str, object]] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        self.details = details or []


class ValidationError(PlatformError):
    """Raised when request data fails validation."""

    def __init__(
        self,
        message: str = "Validation failed",
        details: list[dict[str, object]] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            error_code="VALIDATION_ERROR",
            status_code=400,
            details=details,
        )


class NotFoundError(PlatformError):
    """Raised when a requested resource is not found."""

    def __init__(
        self,
        message: str = "Resource not found",
        details: list[dict[str, object]] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            error_code="NOT_FOUND",
            status_code=404,
            details=details,
        )


class ConflictError(PlatformError):
    """Raised when a resource conflict occurs (e.g. duplicate)."""

    def __init__(
        self,
        message: str = "Resource conflict",
        details: list[dict[str, object]] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            error_code="CONFLICT",
            status_code=409,
            details=details,
        )


class AuthorizationError(PlatformError):
    """Raised when a request is not authorized."""

    def __init__(
        self,
        message: str = "Not authorized",
        details: list[dict[str, object]] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            error_code="AUTHORIZATION_ERROR",
            status_code=403,
            details=details,
        )


class RateLimitError(PlatformError):
    """Raised when a rate limit is exceeded."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        retry_after: int = 60,
        details: list[dict[str, object]] | None = None,
    ) -> None:
        super().__init__(
            message=message,
            error_code="RATE_LIMIT_EXCEEDED",
            status_code=429,
            details=details,
        )
        self.retry_after = retry_after
