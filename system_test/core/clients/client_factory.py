from system_test.core.clients.external.auth.auth_api_client import AuthApiClient
from system_test.core.clients.external.charging_points.charging_points_client import (
    ChargingPointsApiClient,
)
from system_test.core.system_test_configuration import SystemTestConfiguration

from system_test.core.clients.system.ui.car_charging_reservation_ui_client import (
    CarChargingReservationUiClient,
)
from playwright.sync_api import Page


class ClientFactory:
    @staticmethod
    def create_auth_api_client() -> AuthApiClient:
        return AuthApiClient.create(SystemTestConfiguration.get_auth_api_base_url())

    @staticmethod
    def create_charging_points_api_client() -> ChargingPointsApiClient:
        return ChargingPointsApiClient.create(
            SystemTestConfiguration.get_charging_points_base_url()
        )

    @staticmethod
    def create_car_charging_reservation_api_client():
        """Create API client with configuration"""
        from system_test.core.clients.system.api.car_charging_reservation_api_client import (
            CarChargingReservationApiClient,
        )
        base_url = SystemTestConfiguration.get_car_charging_reservation_api_base_url()
        return CarChargingReservationApiClient.create(base_url)

    @staticmethod
    def create_car_charging_reservation_ui_client(
        page: Page,
    ) -> CarChargingReservationUiClient:
        """Create UI client with configuration"""
        base_url = SystemTestConfiguration.get_car_charging_reservation_ui_base_url()
        return CarChargingReservationUiClient.create(page, base_url)
