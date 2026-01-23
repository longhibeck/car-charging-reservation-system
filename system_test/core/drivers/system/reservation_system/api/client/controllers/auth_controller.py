import httpx

from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.system.commons.dtos.auth_response import (
    UserData,
    LoginResponse,
)
from system_test.core.drivers.system.commons.dtos.auth_request import LoginRequest
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils


class AuthController:
    """Controller for Authentication API endpoints"""

    AUTH_PATH = "/api/v1/auth"

    def __init__(self, http_client: HttpTestClient):
        self._http_client = http_client

    def login(self, request: LoginRequest) -> Result[LoginResponse]:
        response = self._http_client.post(f"{self.AUTH_PATH}/login", request)
        return HttpTestUtils.get_ok_result_or_failure(response)

    # def get_current_user(self) -> httpx.Response:
    #     """Get current authenticated user details"""
    #     return self._http_client.get(f"{self.AUTH_PATH}/me")

    # # Helper methods
    # def get_access_token(self, login_response: httpx.Response) -> str:
    #     """Extract access token from login response"""
    #     data: LoginResponse = self._http_client.read_body(login_response)
    #     return data["access_token"]

    # def get_refresh_token(self, login_response: httpx.Response) -> str:
    #     """Extract refresh token from login response"""
    #     data: LoginResponse = self._http_client.read_body(login_response)
    #     return data["refresh_token"]

    # def get_user_from_login(self, login_response: httpx.Response) -> UserData:
    #     """Extract user data from login response"""
    #     data: LoginResponse = self._http_client.read_body(login_response)
    #     return data["user"]

    # def get_error_message(self, response: httpx.Response) -> str:
    #     """Extract error message from failed response"""
    #     return str(response.json())
