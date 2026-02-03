from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils  

class HealthController:
    ENDPOINT = "/health"

    def __init__(self, http_client: HttpTestClient):
        self._http_client = http_client

    def check_health(self):
        response = self._http_client.get(f"{self.ENDPOINT}")
        return HttpTestUtils.get_ok_result_or_failure(response)
    
  