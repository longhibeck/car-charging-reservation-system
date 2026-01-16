from typing import TypeVar
from httpx import Response as HttpxResponse

T = TypeVar("T")


class TypedResponse[T]:
    """
    A generic wrapper around httpx.Response that preserves type information.
    
    Usage:
        response = httpx.get("...")
        typed_response = TypedResponse[CarDto](response)
        data: CarDto = typed_response.json()
    """
    
    def __init__(self, response: HttpxResponse):
        self._response = response
    
    def json(self) -> T:
        """Parse response body as JSON and return as type T."""
        return self._response.json()
    
    @property
    def status_code(self) -> int:
        """HTTP status code."""
        return self._response.status_code
    
    @property
    def text(self) -> str:
        """Response body as text."""
        return self._response.text
    
    @property
    def content(self) -> bytes:
        """Response body as bytes."""
        return self._response.content
    
    @property
    def headers(self):
        """Response headers."""
        return self._response.headers
    
    @property
    def cookies(self):
        """Response cookies."""
        return self._response.cookies
    
    def is_success(self) -> bool:
        """Check if status code is 2xx."""
        return self._response.is_success
    
    def is_error(self) -> bool:
        """Check if status code is 4xx or 5xx."""
        return self._response.is_error
    
    def raise_for_status(self) -> None:
        """Raise HTTPStatusError if status is 4xx or 5xx."""
        self._response.raise_for_status()
    
    @property
    def unwrap(self) -> HttpxResponse:
        """Get the underlying httpx.Response object."""
        return self._response
