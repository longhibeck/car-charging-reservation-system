from __future__ import annotations

import httpx

from system_test.core.clients.commons.http_test_client import HttpTestClient
from system_test.core.clients.system.api.dtos.auth_response import (
    LoginResponse,
    CurrentUserResponse,
    UserData,
)


class AuthController:
    """Controller for Authentication API endpoints"""

    ENDPOINT = "/api/v1/auth"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    # Action methods - make API calls
    def login(self, username: str, password: str) -> httpx.Response:
        """Login with username and password"""
        request = {
            "username": username,
            "password": password,
        }
        return self.http_client.post(f"{self.ENDPOINT}/login", request)

    def get_current_user(self) -> httpx.Response:
        """Get current authenticated user details"""
        return self.http_client.get(f"{self.ENDPOINT}/me")

    # Assertion methods - verify responses
    def assert_login_successful(self, response: httpx.Response) -> LoginResponse:
        """Assert login was successful and return auth data"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    def assert_login_failed(self, response: httpx.Response) -> None:
        """Assert login failed with unauthorized status"""
        self.http_client.assert_unauthorized(response)

    def assert_current_user_retrieved(self, response: httpx.Response) -> CurrentUserResponse:
        """Assert current user was retrieved and return user data"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    # Helper methods
    def get_access_token(self, login_response: httpx.Response) -> str:
        """Extract access token from login response"""
        data: LoginResponse = self.http_client.read_body(login_response)
        return data["access_token"]

    def get_refresh_token(self, login_response: httpx.Response) -> str:
        """Extract refresh token from login response"""
        data: LoginResponse = self.http_client.read_body(login_response)
        return data["refresh_token"]

    def get_user_from_login(self, login_response: httpx.Response) -> UserData:
        """Extract user data from login response"""
        data: LoginResponse = self.http_client.read_body(login_response)
        return data["user"]

    def get_error_message(self, response: httpx.Response) -> str:
        """Extract error message from failed response"""
        return str(response.json())
