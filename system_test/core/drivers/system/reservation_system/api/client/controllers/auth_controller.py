from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils
from system_test.core.drivers.commons.clients.typed_response import TypedResponse
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.system.commons.dtos.auth_request import (
    LoginRequest,
)
from system_test.core.drivers.system.commons.dtos.auth_response import (
    CurrentUserResponse,
    LoginResponse,
)


class AuthController:
    AUTH_PATH = "/api/v1/auth"

    def __init__(self, http_client: HttpTestClient):
        self._http_client = http_client

    def login(self, request: LoginRequest) -> Result[LoginResponse]:
        response: TypedResponse = self._http_client.post(
            f"{self.AUTH_PATH}/login", request
        )
        return HttpTestUtils.get_ok_result_or_failure(response)

    def get_current_user(self) -> Result[CurrentUserResponse]:
        response: TypedResponse = self._http_client.get(f"{self.AUTH_PATH}/me")
        return HttpTestUtils.get_ok_result_or_failure(response)
