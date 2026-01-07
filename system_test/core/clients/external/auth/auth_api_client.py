from system_test.core.clients.commons.http_test_client import HttpTestClient
from system_test.core.clients.external.auth.controllers.login_controller import (
    LoginController,
)
from system_test.core.clients.external.auth.controllers.home_controller import (
    HomeController,
)


class AuthApiClient:
    def __init__(
        self,
        test_http_client: HttpTestClient,
        home_controller: HomeController,
        login_controller: LoginController,
    ):
        self.test_http_client = test_http_client
        self.home_controller = home_controller
        self.login_controller = login_controller

    @staticmethod
    def create(base_url: str):
        test_http_client = HttpTestClient(base_url)
        home_controller = HomeController(test_http_client)
        login_controller = LoginController(test_http_client)
        return AuthApiClient(test_http_client, home_controller, login_controller)

    def home(self) -> HomeController:
        return self.home_controller

    def login(self) -> LoginController:
        return self.login_controller
