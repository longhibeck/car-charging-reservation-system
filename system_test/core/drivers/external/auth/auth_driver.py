from typing import Protocol
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.external.auth.dtos.login_response import LoginResponse
from system_test.core.drivers.external.auth.dtos.current_user_response import CurrentUserResponse
from system_test.core.drivers.external.auth.dtos.error.auth_error_response import AuthErrorResponse

class AuthDriver(Protocol):
    def go_to_auth(self) -> Result[None]: ...

    def login(self, username: str, password: str) -> Result[LoginResponse | AuthErrorResponse]: ...

    def get_current_user(self) -> Result[CurrentUserResponse | AuthErrorResponse]: ...

    def close(self) -> None: ...