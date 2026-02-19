from system_test.core.drivers.external.charging_points.client.charging_points_api_client import ChargingPointsApiClient
from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.closer import Closer
from httpx import Client


class ChargingPointsDriver:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self._http_client = Client(base_url=base_url, headers={"Content-Type": "application/json"})
        http_test_client = HttpTestClient(self._http_client, base_url)
        self._api_client = ChargingPointsApiClient(http_test_client)

    def go_to_charging_points(self):
        return self._api_client.health().check_health()

    def list_charging_points(self):
        return self._api_client.charging_points().list_charging_points()
    
    def get_charging_point(self, charging_point_id: str):
        return self._api_client.charging_points().get_charging_point(charging_point_id)
    
    def close(self) -> None:
        Closer.close(self._http_client)
    