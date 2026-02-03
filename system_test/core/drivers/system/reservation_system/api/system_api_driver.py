from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.commons.clients.http_client_factory import (
    HttpClientFactory,
)
from system_test.core.drivers.system.commons.dtos.car_request import AddCarRequest
from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.drivers.system.commons.dtos.reservation_response import ReservationResponse
from system_test.core.drivers.system.commons.dtos.auth_request import LoginRequest
from system_test.core.drivers.system.reservation_system.api.client.system_api_client import (
    SystemApiClient,
)

# from httpx import Client


class SystemApiDriver(SystemDriver):
    def __init__(self, base_url) -> None:
        self._http_client = HttpClientFactory.create(base_url)
        self._client = SystemApiClient(self._http_client, base_url)

    def go_to_system(self) -> None:
        return self._client.health.check_health()

    def login(self, username: str, password: str) -> Result[str]:
        request = LoginRequest(username=username, password=password)
        result = self._client.auth.login(request)
        
        # Auto-configure authentication on successful login
        if result.is_success():
            login_response = result.get_value()
            self._http_client.headers["Authorization"] = f"Bearer {login_response['access_token']}"
        
        return result
    
    def get_current_user(self) -> Result[str]:
        result = self._client.auth.get_current_user()
        return result

    def add_car(
        self,
        name: str,
        connector_types: list[str],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> AddCarResponse:
        request = AddCarRequest(
            name=name,
            connector_types=connector_types,
            battery_charge_limit=battery_charge_limit,
            battery_size=battery_size,
            max_kw_ac=max_kw_ac,
            max_kw_dc=max_kw_dc,
        )
        return self._client.car.add_car(request)
    
    def update_car(
        self,
        car_id: str,
        name: str,
        connector_types: list[str],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> Result[None]:
        request = AddCarRequest(
            name=name,
            connector_types=connector_types,
            battery_charge_limit=battery_charge_limit,
            battery_size=battery_size,
            max_kw_ac=max_kw_ac,
            max_kw_dc=max_kw_dc,
        )
        return self._client.car.update_car(car_id, request)
    
    def delete_car(self, car_id: str) -> Result[None]:
        return self._client.car.delete_car(car_id)

    def list_cars(self) -> Result[list[AddCarResponse]]:
        return self._client.car.list_cars()
    
    def get_car(self, car_id: str) -> Result[AddCarResponse]:
        return self._client.car.get_car(car_id)
    
    def list_reservations(self) -> Result[list[ReservationResponse]]:
        return self._client.reservation.list_reservations()
    
    def get_reservation(self, reservation_id: int) -> Result[ReservationResponse]:
        return self._client.reservation.get_reservation(reservation_id)
    
    def create_reservation(
        self,
        car_id: str,
        charging_point_id: str,
        start_time: str,
        end_time: str,
    ) -> Result[ReservationResponse]:
        return self._client.reservation.create_reservation(
            car_id, charging_point_id, start_time, end_time
        )
