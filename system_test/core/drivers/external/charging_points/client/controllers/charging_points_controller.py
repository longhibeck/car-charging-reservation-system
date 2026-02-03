from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils
from system_test.core.drivers.commons.result import Result


class ChargingPointsController:
    ENDPOINT = "/api/v1/charging-points"

    def __init__(self, http_client: HttpTestClient):
        self._http_client = http_client

    def list_charging_points(self):
        response = self._http_client.get(f"{self.ENDPOINT}/")
        result = HttpTestUtils.get_ok_result_or_failure(response)
        if result.is_failure():
            return Result.failure(result.get_error_messages())
        return Result.success()

    def get_charging_point(self, charging_point_id: str):
        response = self._http_client.get(f"{self.ENDPOINT}/{charging_point_id}")
        result = HttpTestUtils.get_ok_result_or_failure(response)
        if result.is_failure():
            return Result.failure(result.get_error_messages())
        return Result.success()
