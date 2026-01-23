
import system_test
from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.system.reservation_system.api.client.controllers.health_controller import HealthController
from system_test.core.drivers.system.reservation_system.api.client.controllers.car_controller import CarController
from system_test.core.drivers.system.reservation_system.api.client.controllers.auth_controller import AuthController
from system_test.core.drivers.system.reservation_system.api.client.controllers.reservation_controller import ReservationController
from httpx import Client


class SystemApiClient:
    def __init__(self, client:Client, base_url:str) -> None:
        self._http_client = client
        self._http_test_client = HttpTestClient(client, base_url)
        self.health = HealthController(self._http_test_client)
        self.car = CarController(self._http_test_client)
        self.auth = AuthController(self._http_test_client)
        self.reservation = ReservationController(self._http_test_client)