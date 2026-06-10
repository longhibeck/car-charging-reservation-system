from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils
from system_test.core.drivers.commons.clients.typed_response import TypedResponse
from system_test.core.drivers.commons.result import Result


class HealthController:
    HEALTH_PATH = "/health"

    def __init__(self, http_client: HttpTestClient):
        self._http_client = http_client

    def check_health(self) -> Result[None]:
        response: TypedResponse = self._http_client.get(self.HEALTH_PATH)
        return HttpTestUtils.get_ok_result_or_failure(response)
