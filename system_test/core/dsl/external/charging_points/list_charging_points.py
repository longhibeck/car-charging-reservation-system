from system_test.core.drivers.external.charging_points.charging_points_driver import (
    ChargingPointsDriver,
)
from system_test.core.drivers.external.charging_points.dtos.get_charging_point_response import (
    GetChargingPointResponse,
)
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class ListChargingPointsVerification(
    ResponseVerification[list[GetChargingPointResponse]]
):
    """Assertions on a list-charging-points result.

    Example
    -------
    .execute().should_succeed().is_not_empty()
    """

    def is_not_empty(self) -> "ListChargingPointsVerification":
        assert self._response, (
            "Expected at least one charging point but the list was empty"
        )
        return self

    def has_count(self, expected: int) -> "ListChargingPointsVerification":
        assert len(self._response) == expected, (
            f"Expected {expected} charging points but got {len(self._response)}"
        )
        return self


class ListChargingPoints(
    BaseUseCase[
        ChargingPointsDriver,
        list[GetChargingPointResponse],
        ListChargingPointsVerification,
    ]
):
    """Use case: retrieve all charging points.

    Example
    -------
    app.charging_points().list_charging_points().execute().should_succeed()
    """

    def execute(
        self,
    ) -> UseCaseResult[list[GetChargingPointResponse], ListChargingPointsVerification]:
        result = self._driver.list_charging_points()
        return UseCaseResult(result, self._context, ListChargingPointsVerification)
