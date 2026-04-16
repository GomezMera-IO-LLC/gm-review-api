"""Standardized API response builders matching the design error format.

Error format:
{
    "error": {
        "code": "VALIDATION_ERROR",
        "message": "...",
        "details": [{"field": "rating", "message": "...", "value": 7}],
        "requestId": "req_abc123",
        "timestamp": "2024-01-15T10:30:00Z"
    }
}

Success format:
{
    "data": { ... },
    "metadata": { ... }    // optional
}
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from src.shared.exceptions import PlatformError


def error_response(
    status_code: int,
    error_code: str,
    message: str,
    details: list[dict[str, object]] | None = None,
    request_id: str | None = None,
) -> dict[str, Any]:
    """Build a standardised error response.

    Args:
        status_code: HTTP status code.
        error_code: Machine-readable error code (e.g. VALIDATION_ERROR).
        message: Human-readable error message.
        details: Optional list of field-level error details.
        request_id: Optional request ID for tracing.

    Returns:
        API Gateway-compatible response dict with statusCode, headers, and body.
    """
    body: dict[str, Any] = {
        "error": {
            "code": error_code,
            "message": message,
            "details": details or [],
            "requestId": request_id or "",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
    }
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }


def error_response_from_exception(
    exc: PlatformError,
    request_id: str | None = None,
) -> dict[str, Any]:
    """Build an error response from a PlatformError."""
    return error_response(
        status_code=exc.status_code,
        error_code=exc.error_code,
        message=exc.message,
        details=exc.details,
        request_id=request_id,
    )


def success_response(
    data: Any,
    status_code: int = 200,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a standardised success response.

    Args:
        data: Response payload.
        status_code: HTTP status code (default 200).
        metadata: Optional metadata (pagination, etc.).

    Returns:
        API Gateway-compatible response dict.
    """
    body: dict[str, Any] = {"data": data}
    if metadata is not None:
        body["metadata"] = metadata
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
