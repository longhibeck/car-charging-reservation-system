from __future__ import annotations

import httpx

from system_test.core.clients.commons.http_test_client import HttpTestClient
from system_test.core.clients.system.api.dtos import (
    CreateCarRequest,
    UpdateCarRequest,
    CarResponse,
)
from system_test.core.clients.system.api.enums import (
    ConnectorTypeLiteral,
)


class CarController:
    """Controller for Car API endpoints"""

    ENDPOINT = "/api/v1/cars"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    # Action methods - make API calls
    def create_car(
        self,
        name: str,
        connector_types: list[ConnectorTypeLiteral],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> httpx.Response:
        """Create a new car"""
        request: CreateCarRequest = {
            "name": name,
            "connector_types": connector_types,
            "battery_charge_limit": battery_charge_limit,
            "battery_size": battery_size,
            "max_kw_ac": max_kw_ac,
            "max_kw_dc": max_kw_dc,
        }
        return self.http_client.post(f"{self.ENDPOINT}/", request)

    def list_cars(self) -> httpx.Response:
        """Get list of all cars"""
        return self.http_client.get(f"{self.ENDPOINT}/")

    def get_car(self, car_id: int) -> httpx.Response:
        """Get a specific car by ID"""
        return self.http_client.get(f"{self.ENDPOINT}/{car_id}")

    def update_car(
        self,
        car_id: int,
        name: str,
        connector_types: list[ConnectorTypeLiteral],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> httpx.Response:
        """Update an existing car"""
        request: UpdateCarRequest = {
            "name": name,
            "connector_types": connector_types,
            "battery_charge_limit": battery_charge_limit,
            "battery_size": battery_size,
            "max_kw_ac": max_kw_ac,
            "max_kw_dc": max_kw_dc,
        }
        return self.http_client.put(f"{self.ENDPOINT}/{car_id}", request)

    def delete_car(self, car_id: int) -> httpx.Response:
        """Delete a car"""
        return self.http_client.post(f"{self.ENDPOINT}/{car_id}/delete")

    # Assertion methods - verify responses
    def assert_car_created_successfully(self, response: httpx.Response) -> CarResponse:
        """Assert car was created and return the car data"""
        self.http_client.assert_created(response)
        return self.http_client.read_body(response)

    def assert_car_creation_failed(self, response: httpx.Response) -> None:
        """Assert car creation failed with validation error"""
        self.http_client.assert_unprocessable_entity(response)

    def assert_car_retrieved_successfully(
        self, response: httpx.Response
    ) -> CarResponse:
        """Assert car was retrieved and return the car data"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    def assert_cars_listed_successfully(
        self, response: httpx.Response
    ) -> list[CarResponse]:
        """Assert cars were listed and return the list"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    def assert_car_updated_successfully(self, response: httpx.Response) -> CarResponse:
        """Assert car was updated and return the car data"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    def assert_car_deleted_successfully(self, response: httpx.Response) -> None:
        """Assert car was deleted"""
        self.http_client.assert_no_content(response)

    def assert_unauthenticated_access_denied(self, response: httpx.Response) -> None:
        """Assert access is denied for unauthenticated requests"""
        self.http_client.assert_unauthorized(response)

    # Helper methods
    def get_error_message(self, response: httpx.Response) -> str:
        """Extract error message from failed response"""
        return str(response.json())
