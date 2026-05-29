from typing import TypedDict


class CurrentUserResponse(TypedDict):
    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str
