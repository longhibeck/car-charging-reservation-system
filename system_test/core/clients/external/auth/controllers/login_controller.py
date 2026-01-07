from system_test.core.clients.commons.http_test_client import HttpTestClient
from system_test.core.clients.external.auth.dtos.login_request import LoginRequest


class LoginController:
    ENDPOINT = "/auth/login"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    def post_login(self, username: str, password: str):
        request = LoginRequest(username=username, password=password)
        response = self.http_client.post(LoginController.ENDPOINT, request)
        return response

    def assert_login_successful(self, response):
        self.http_client.assert_ok(response)
    
    def assert_login_failed(self, response):
        self.http_client.assert_bad_request(response)
           