from system_test.core.drivers.system.commons.dtos.reservation_response import (
    ReservationResponse,
)
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.system.get_reservation import GetReservationVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenGetReservationImpl(
    BaseWhenStepImpl[ReservationResponse, GetReservationVerification]
):
    """When step: retrieve a single reservation by ID.

    Example
    -------
    scenario.when().get_reservation().reservation_id("res1")
        .then().should_succeed().has_status("active").has_car_id("car1")
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().get_reservation()

    def reservation_id(self, alias: str) -> "WhenGetReservationImpl":
        self._use_case.reservation_id(alias)
        return self

    def _execute(
        self,
    ) -> UseCaseResult[ReservationResponse, GetReservationVerification]:
        return self._use_case.execute()
