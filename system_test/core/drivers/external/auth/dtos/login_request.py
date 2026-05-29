from typing import TypedDict, NotRequired

class LoginRequest(TypedDict):
    username: str
    password: str
    expireInMins: NotRequired[int]
