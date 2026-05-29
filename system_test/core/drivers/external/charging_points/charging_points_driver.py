from typing import Protocol
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.external.charging_points.dtos.get_charging_point_request import GetChargingPointRequest
from system_test.core.drivers.external.charging_points.dtos.get_charging_point_response import (
    GetChargingPointResponse,
)
from system_test.core.drivers.external.charging_points.dtos.error.charging_points_error_response import (
    ChargingPointsErrorResponse,
)


class ChargingPointsDriver(Protocol):
    def go_to_charging_points(self) -> Result[None]: ...

    def list_charging_points(
        self,
    ) -> Result[list[GetChargingPointResponse] | ChargingPointsErrorResponse]: ...

    def get_charging_point(
        self, request: GetChargingPointRequest
    ) -> Result[GetChargingPointResponse | ChargingPointsErrorResponse]: ...

    def close(self) -> None: ...
