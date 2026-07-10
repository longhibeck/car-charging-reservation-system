from system_test.core.drivers.system.commons.dtos.reservation_response import (
    ReservationResponse,
)
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.system.list_reservations import ListReservationsVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenListReservationsImpl(
    BaseWhenStepImpl[list[ReservationResponse], ListReservationsVerification]
):
    """When step: list all reservations for the authenticated user.

    Example
    -------
    scenario.when().list_reservations().then().should_succeed().is_not_empty()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().list_reservations()

    def _execute(
        self,
    ) -> UseCaseResult[list[ReservationResponse], ListReservationsVerification]:
        return self._use_case.execute()
