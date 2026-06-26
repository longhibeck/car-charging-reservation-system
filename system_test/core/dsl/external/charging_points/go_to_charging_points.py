from system_test.core.drivers.external.charging_points.charging_points_driver import (
    ChargingPointsDriver,
)
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification


class GoToChargingPoints:
    """Use case: check the charging-points service is reachable.

    Example
    -------
    app.charging_points().go_to_charging_points().execute().should_succeed()
    """

    def __init__(self, driver: ChargingPointsDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def execute(self) -> UseCaseResult[None, VoidVerification]:
        result = self._driver.go_to_charging_points()
        return UseCaseResult(result, self._context, VoidVerification)
