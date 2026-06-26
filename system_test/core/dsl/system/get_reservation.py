from system_test.core.drivers.system.commons.dtos.reservation_response import (
    ReservationResponse,
)
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class GetReservationVerification(ResponseVerification[ReservationResponse]):
    """Assertions on a get-reservation result.

    Example
    -------
    .execute().should_succeed().has_status("active")
    """

    def has_status(self, expected: str) -> "GetReservationVerification":
        assert self._response["status"] == expected, (
            f"Expected reservation status '{expected}' but got '{self._response['status']}'"
        )
        return self


class GetReservation(
    BaseUseCase[SystemDriver, ReservationResponse, GetReservationVerification]
):
    """Use case: retrieve a single reservation by ID.

    reservation_id() resolves from the context result map — pass the same
    alias used in the preceding create_reservation() call.

    Example
    -------
    app.system().get_reservation().reservation_id("res1").execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        super().__init__(driver, context)
        self._reservation_id_alias: str | None = None

    def reservation_id(self, alias: str) -> "GetReservation":
        self._reservation_id_alias = alias
        return self

    def execute(self) -> UseCaseResult[ReservationResponse, GetReservationVerification]:
        reservation_id = self._context.get_result_value(self._reservation_id_alias)
        result = self._driver.get_reservation(reservation_id)
        return UseCaseResult(result, self._context, GetReservationVerification)
