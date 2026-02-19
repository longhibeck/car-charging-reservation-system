from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.system.commons.dtos.reservation_request import ReservationRequest
from system_test.core.drivers.system.commons.dtos.reservation_response import ReservationResponse
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.commons.clients.http_test_utils import HttpTestUtils

class ReservationController:
    """Controller for Reservation API endpoints"""

    RESERVATIONS_PATH = "/api/v1/reservations"

    def __init__(self, http_client: HttpTestClient):
        self._http_client = http_client

    # Action methods - make API calls
    def create_reservation(
        self,
        car_id: int,
        charging_point_id: str,
        start_time: str,
        end_time: str,
    ) -> Result[ReservationResponse]:
        request = ReservationRequest(
            car_id=car_id,
            charging_point_id=charging_point_id,
            start_time=start_time,
            end_time=end_time,
        )
        response = self._http_client.post(f"{self.RESERVATIONS_PATH}/", request)
        return HttpTestUtils.get_created_result_or_failure(response)

    def list_reservations(self) -> Result[list[ReservationResponse]]:
        response = self._http_client.get(f"{self.RESERVATIONS_PATH}/")
        return HttpTestUtils.get_ok_result_or_failure(response)
    
    def get_reservation(self, reservation_id: int) -> Result[ReservationResponse]:
        response = self._http_client.get(f"{self.RESERVATIONS_PATH}/{reservation_id}")
        return HttpTestUtils.get_ok_result_or_failure(response)
    # def update_reservation(
    #     self,
    #     reservation_id: int,
    #     car_id: int,
    #     charging_point_id: str,
    #     start_time: str,
    #     end_time: str,
    # ) -> httpx.Response:
    #     """Update an existing reservation"""
    #     request: dict[str, Any] = {
    #         "car_id": car_id,
    #         "charging_point_id": charging_point_id,
    #         "start_time": start_time,
    #         "end_time": end_time,
    #     }
    #     return self._http_client.post(
    #         f"{self.RESERVATIONS_PATH}/{reservation_id}", request
    #     )

    # def cancel_reservation(self, reservation_id: int) -> httpx.Response:
    #     """Cancel a reservation"""
    #     return self._http_client.post(
    #         f"{self.RESERVATIONS_PATH}/{reservation_id}/cancel"
    #     )

    # def delete_reservation(self, reservation_id: int) -> httpx.Response:
    #     """Delete a reservation"""
    #     return self._http_client.post(
    #         f"{self.RESERVATIONS_PATH}/{reservation_id}/delete"
    #     )