from __future__ import annotations

from typing import Any

import httpx

from system_test.core.clients.commons.http_test_client import HttpTestClient
from system_test.core.clients.system.api.dtos.reservation_response import (
    ReservationResponse,
)


class ReservationController:
    """Controller for Reservation API endpoints"""

    ENDPOINT = "/api/v1/reservations"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    # Action methods - make API calls
    def create_reservation(
        self,
        car_id: int,
        charging_point_id: str,
        start_time: str,
        end_time: str,
    ) -> httpx.Response:
        """Create a new reservation"""
        request: dict[str, Any] = {
            "car_id": car_id,
            "charging_point_id": charging_point_id,
            "start_time": start_time,
            "end_time": end_time,
        }
        return self.http_client.post(f"{self.ENDPOINT}/", request)

    def list_reservations(self) -> httpx.Response:
        """Get list of all reservations"""
        return self.http_client.get(f"{self.ENDPOINT}/")

    def get_reservation(self, reservation_id: int) -> httpx.Response:
        """Get a specific reservation by ID"""
        return self.http_client.get(f"{self.ENDPOINT}/{reservation_id}")

    def update_reservation(
        self,
        reservation_id: int,
        car_id: int,
        charging_point_id: str,
        start_time: str,
        end_time: str,
    ) -> httpx.Response:
        """Update an existing reservation"""
        request: dict[str, Any] = {
            "car_id": car_id,
            "charging_point_id": charging_point_id,
            "start_time": start_time,
            "end_time": end_time,
        }
        return self.http_client.post(f"{self.ENDPOINT}/{reservation_id}", request)

    def cancel_reservation(self, reservation_id: int) -> httpx.Response:
        """Cancel a reservation"""
        return self.http_client.post(f"{self.ENDPOINT}/{reservation_id}/cancel")

    def delete_reservation(self, reservation_id: int) -> httpx.Response:
        """Delete a reservation"""
        return self.http_client.post(f"{self.ENDPOINT}/{reservation_id}/delete")

    # Assertion methods - verify responses
    def assert_reservation_created_successfully(
        self, response: httpx.Response
    ) -> ReservationResponse:
        """Assert reservation was created and return the reservation data"""
        self.http_client.assert_created(response)
        return self.http_client.read_body(response)

    def assert_reservation_creation_failed(self, response: httpx.Response) -> None:
        """Assert reservation creation failed with validation error"""
        self.http_client.assert_unprocessable_entity(response)

    def assert_reservation_retrieved_successfully(
        self, response: httpx.Response
    ) -> ReservationResponse:
        """Assert reservation was retrieved and return the reservation data"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    def assert_reservations_listed_successfully(
        self, response: httpx.Response
    ) -> list[ReservationResponse]:
        """Assert reservations were listed and return the list"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    def assert_reservation_updated_successfully(
        self, response: httpx.Response
    ) -> ReservationResponse:
        """Assert reservation was updated and return the reservation data"""
        self.http_client.assert_ok(response)
        return self.http_client.read_body(response)

    def assert_reservation_cancelled_successfully(
        self, response: httpx.Response
    ) -> None:
        """Assert reservation was cancelled"""
        self.http_client.assert_ok(response)

    def assert_reservation_deleted_successfully(self, response: httpx.Response) -> None:
        """Assert reservation was deleted"""
        self.http_client.assert_no_content(response)

    def assert_unauthenticated_access_denied(self, response: httpx.Response) -> None:
        """Assert access is denied for unauthenticated requests"""
        self.http_client.assert_unauthorized(response)

    # Helper methods
    def get_error_message(self, response: httpx.Response) -> str:
        """Extract error message from failed response"""
        return str(response.json())
