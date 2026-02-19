from typing import TypedDict


class UserData(TypedDict):
    id: int
    username: str
    external_user_id: int


class LoginResponse(TypedDict):
    access_token: str
    refresh_token: str
    token_type: str
    user: UserData


class CurrentUserResponse(TypedDict):
    id: int
    username: str
    external_user_id: int
