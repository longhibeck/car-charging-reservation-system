from typing import Protocol
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.drivers.system.commons.dtos.auth_response import LoginResponse
from system_test.core.drivers.system.commons.dtos.reservation_response import (
    ReservationResponse,
)
from system_test.core.drivers.system.commons.enums.connector_type import (
    ConnectorTypeLiteral,
)


class SystemDriver(Protocol):
    def go_to_system(self) -> Result[None]: ...
    
    def login(self, username: str, password: str) -> Result[LoginResponse]: ...
    
    def add_car(
        self,
        car_name: str,
        connector_types: list[ConnectorTypeLiteral],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> Result[AddCarResponse]: ...

    def list_cars(self) -> Result[list[AddCarResponse]]: ...

    def get_car(self, car_id: str) -> Result[AddCarResponse]: ...

    def list_reservations(self) -> Result[list[ReservationResponse]]: ...

    def get_reservation(self, reservation_id: int) -> Result[ReservationResponse]: ...
