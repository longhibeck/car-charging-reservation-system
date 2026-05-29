from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.external.auth.dtos.login_request import LoginRequest
from system_test.core.drivers.external.auth.dtos.login_response import LoginResponse
from system_test.core.drivers.external.auth.dtos.current_user_response import CurrentUserResponse


class AuthController:
    ENDPOINT = "/auth"

    def __init__(self, http_client: HttpTestClient):
        self._http_client = http_client

    def login(self, username: str, password: str) -> Result[LoginResponse]:
        request = LoginRequest(username=username, password=password)
        response = self._http_client.post(f"{self.ENDPOINT}/login", request)
        result = HttpTestUtils.get_ok_result_or_failure(response)
        if result.is_failure():
            return Result.failure(result.get_error_messages())
        return Result.success(result.get_value())

    def get_current_user(self) -> Result[CurrentUserResponse]:
        response = self._http_client.get(f"{self.ENDPOINT}/me")
        result = HttpTestUtils.get_ok_result_or_failure(response)
        if result.is_failure():
            return Result.failure(result.get_error_messages())
        return Result.success(result.get_value())
