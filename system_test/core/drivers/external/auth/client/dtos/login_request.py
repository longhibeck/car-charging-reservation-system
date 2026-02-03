from typing import TypedDict


class LoginRequest(TypedDict):
    username: str
    password: str
