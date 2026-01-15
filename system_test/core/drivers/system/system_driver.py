from typing import Protocol
from system_test.core.drivers.system.commons.result import Result
from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.drivers.system.commons.enums.connector_type import (
    ConnectorTypeLiteral,
)
class SystemDriver(Protocol):
    def go_to_system(self) -> Result[None]: ...

    def add_car(
        self,
        car_name: str,
        connector_types: list[ConnectorTypeLiteral],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> Result[AddCarResponse]: ...
