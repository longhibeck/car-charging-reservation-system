from system_test.core.drivers.system.commons.dtos.reservation_response import (
    ReservationResponse,
)
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.system.create_reservation import CreateReservationVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenCreateReservationImpl(
    BaseWhenStepImpl[ReservationResponse, CreateReservationVerification]
):
    """When step: create a charging reservation.

    Example
    -------
    scenario.when().create_reservation()
        .reservation_id("res1").car_id("car1").charging_point_id(CP_ID)
        .then().should_succeed().has_status("active")
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().create_reservation()

    def reservation_id(self, alias: str) -> "WhenCreateReservationImpl":
        self._use_case.reservation_id(alias)
        return self

    def car_id(self, alias: str) -> "WhenCreateReservationImpl":
        self._use_case.car_id(alias)
        return self

    def charging_point_id(self, value: str) -> "WhenCreateReservationImpl":
        self._use_case.charging_point_id(value)
        return self

    def start_time(self, value: str) -> "WhenCreateReservationImpl":
        self._use_case.start_time(value)
        return self

    def end_time(self, value: str) -> "WhenCreateReservationImpl":
        self._use_case.end_time(value)
        return self

    def _execute(
        self,
    ) -> UseCaseResult[ReservationResponse, CreateReservationVerification]:
        return self._use_case.execute()
