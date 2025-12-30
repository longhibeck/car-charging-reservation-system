from __future__ import annotations

import httpx

from system_test.core.clients.commons.http_test_client import HttpTestClient


class HealthController:
    """Controller for Health API endpoint"""

    ENDPOINT = "/health"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    # Action methods - make API calls
    def get_health(self) -> httpx.Response:
        """Get health status of the service"""
        return self.http_client.get(self.ENDPOINT)

    # Assertion methods - verify responses
    def assert_healthy(self, response: httpx.Response) -> None:
        """Assert service is healthy"""
        self.http_client.assert_ok(response)
