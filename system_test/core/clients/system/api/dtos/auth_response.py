from typing import TypedDict


class UserData(TypedDict):
    """User data within auth response"""
    id: int
    username: str
    external_user_id: int


class LoginResponse(TypedDict):
    """Response DTO for login endpoint"""
    access_token: str
    refresh_token: str
    token_type: str
    user: UserData


class CurrentUserResponse(TypedDict):
    """Response DTO for current user (me) endpoint"""
    id: int
    username: str
    external_user_id: int
