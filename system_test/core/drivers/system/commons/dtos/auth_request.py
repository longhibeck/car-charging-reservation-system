from typing import TypedDict


class LoginRequest(TypedDict):
    """Request DTO for authentication endpoints"""

    username: str
    password: str
