from system_test.core.clients.commons.http_test_client import HttpTestClient
from system_test.core.clients.external.charging_points.controllers.charging_points_controller import (
    ChargingPointsController,
)
from system_test.core.clients.external.charging_points.controllers.home_controller import (
    HomeController,
)


class ChargingPointsApiClient:
    def __init__(
        self,
        test_http_client: HttpTestClient,
        home_controller: HomeController,
        charging_points_controller: ChargingPointsController,
    ):
        self.test_http_client = test_http_client
        self.home_controller = home_controller
        self.charging_points_controller = charging_points_controller

    @staticmethod
    def create(base_url: str):
        test_http_client = HttpTestClient(base_url)
        home_controller = HomeController(test_http_client)
        charging_points_controller = ChargingPointsController(test_http_client)
        return ChargingPointsApiClient(test_http_client, home_controller, charging_points_controller)

    def home(self) -> HomeController:
        return self.home_controller

    def charging_points(self) -> ChargingPointsController:
        return self.charging_points_controller
