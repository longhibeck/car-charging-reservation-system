from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.external.auth.client.controllers.auth_controller import (
    AuthController,
)
from system_test.core.drivers.external.auth.client.controllers.health_controller import (
    HealthController,
)


class AuthApiClient:
    def __init__(self, http_test_client: HttpTestClient) -> None:
        self._http_test_client = http_test_client
        self.health_controller = HealthController(self._http_test_client)
        self.auth_controller = AuthController(self._http_test_client)

    def health(self) -> HealthController:
        return self.health_controller

    def auth(self) -> AuthController:
        return self.auth_controller
