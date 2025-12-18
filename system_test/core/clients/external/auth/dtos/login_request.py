#from dataclasses import dataclass

#@dataclass
#class LoginRequest:
#    username: str
#    password: str

from typing import TypedDict

class LoginRequest(TypedDict):
    username: str
    password: str