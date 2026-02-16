from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.external.charging_points.client.controllers.charging_points_controller import (
    ChargingPointsController,
)
from system_test.core.drivers.system.reservation_system.api.client.controllers.health_controller import (
    HealthController,
)


class ChargingPointsApiClient:
    def __init__(self, http_test_client: HttpTestClient) -> None:
        self._http_test_client = http_test_client
        self.charging_points_controller = ChargingPointsController(
            self._http_test_client
        )
        self.health_controller = HealthController(self._http_test_client)

    def charging_points(self) -> ChargingPointsController:
        return self.charging_points_controller

    def health(self) -> HealthController:
        return self.health_controller
