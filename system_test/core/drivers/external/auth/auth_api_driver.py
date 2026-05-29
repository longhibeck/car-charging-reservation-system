from system_test.core.drivers.external.auth.auth_driver import AuthDriver
from system_test.core.drivers.external.auth.client.auth_api_client import AuthApiClient
from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.closer import Closer
from httpx import Client
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.external.auth.dtos.login_response import LoginResponse
from system_test.core.drivers.external.auth.dtos.login_request import LoginRequest
from system_test.core.drivers.external.auth.dtos.current_user_response import (
    CurrentUserResponse,
)
from system_test.core.drivers.external.auth.dtos.error.auth_error_response import (
    AuthErrorResponse,
)


class AuthApiDriver(AuthDriver):
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self._http_client = Client(
            base_url=base_url, headers={"Content-Type": "application/json"}
        )
        http_test_client = HttpTestClient(self._http_client, base_url)
        self._api_client = AuthApiClient(http_test_client)

    def go_to_auth(self) -> Result[None]:
        return self._api_client.health().check_health()

    def login(self, request: LoginRequest) -> Result[LoginResponse | AuthErrorResponse]:
        return self._api_client.auth().login(request["username"], request["password"])

    def get_current_user(self) -> Result[CurrentUserResponse | AuthErrorResponse]:
        return self._api_client.auth().get_current_user()

    def close(self) -> None:
        Closer.close(self._http_client)
