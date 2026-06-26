from system_test.core.drivers.external.charging_points.charging_points_driver import (
    ChargingPointsDriver,
)
from system_test.core.dsl.external.charging_points.go_to_charging_points import (
    GoToChargingPoints,
)
from system_test.core.dsl.external.charging_points.list_charging_points import (
    ListChargingPoints,
)
from system_test.core.dsl.shared.use_case_context import UseCaseContext


class ChargingPointsDsl:
    """Domain DSL for the external charging-points service.

    One factory method per use case — no logic here, only creation.

    Example
    -------
    app.charging_points().go_to_charging_points().execute().should_succeed()
    app.charging_points().list_charging_points().execute().should_succeed()
    """

    def __init__(self, driver: ChargingPointsDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def go_to_charging_points(self) -> GoToChargingPoints:
        return GoToChargingPoints(self._driver, self._context)

    def list_charging_points(self) -> ListChargingPoints:
        return ListChargingPoints(self._driver, self._context)

    def close(self) -> None:
        self._driver.close()
