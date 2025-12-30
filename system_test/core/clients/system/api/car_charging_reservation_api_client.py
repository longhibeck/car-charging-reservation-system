from system_test.core.clients.commons.http_test_client import HttpTestClient
from system_test.core.clients.system.api.controllers.auth_controller import (
    AuthController,
)
from system_test.core.clients.system.api.controllers.car_controller import (
    CarController,
)
from system_test.core.clients.system.api.controllers.health_controller import (
    HealthController,
)
from system_test.core.clients.system.api.controllers.reservation_controller import (
    ReservationController,
)


class CarChargingReservationApiClient:
    """Main API client for Car Charging Reservation System"""

    def __init__(
        self,
        http_client: HttpTestClient,
        auth_controller: AuthController,
        car_controller: CarController,
        health_controller: HealthController,
        reservation_controller: ReservationController,
    ):
        self.http_client = http_client
        self.auth_controller = auth_controller
        self.car_controller = car_controller
        self.health_controller = health_controller
        self.reservation_controller = reservation_controller

    @staticmethod
    def create(base_url: str) -> "CarChargingReservationApiClient":
        """Create a new API client instance with all controllers"""
        http_client = HttpTestClient(base_url)
        auth_controller = AuthController(http_client)
        car_controller = CarController(http_client)
        health_controller = HealthController(http_client)
        reservation_controller = ReservationController(http_client)

        return CarChargingReservationApiClient(
            http_client,
            auth_controller,
            car_controller,
            health_controller,
            reservation_controller,
        )

    def auth(self) -> AuthController:
        """Get authentication controller"""
        return self.auth_controller

    def cars(self) -> CarController:
        """Get car controller"""
        return self.car_controller

    def health(self) -> HealthController:
        """Get health controller"""
        return self.health_controller

    def reservations(self) -> ReservationController:
        """Get reservation controller"""
        return self.reservation_controller

    def set_auth_token(self, token: str) -> None:
        """Set authentication token for subsequent requests"""
        self.http_client.set_auth_token(token)
