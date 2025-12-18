from system_test.core.clients.commons.http_test_client import HttpTestClient


class ChargingPointsController:
    ENDPOINT = "/api/v1/charging-points"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    def get_charging_points(self):
        response = self.http_client.get(ChargingPointsController.ENDPOINT)
        return response

    def assert_get_charging_points_successful(self, response):
        self.http_client.assert_ok(response)
