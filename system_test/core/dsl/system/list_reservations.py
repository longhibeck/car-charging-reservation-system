from system_test.core.drivers.system.commons.dtos.reservation_response import (
    ReservationResponse,
)
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class ListReservationsVerification(ResponseVerification[list[ReservationResponse]]):
    """Assertions on a list-reservations result.

    Example
    -------
    .execute().should_succeed().is_not_empty()
    """

    def is_not_empty(self) -> "ListReservationsVerification":
        assert self._response, (
            "Expected at least one reservation but the list was empty"
        )
        return self

    def has_count(self, expected: int) -> "ListReservationsVerification":
        assert len(self._response) == expected, (
            f"Expected {expected} reservations but got {len(self._response)}"
        )
        return self


class ListReservations:
    """Use case: retrieve all reservations for the current user.

    Example
    -------
    app.system().list_reservations().execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def execute(
        self,
    ) -> UseCaseResult[list[ReservationResponse], ListReservationsVerification]:
        result = self._driver.list_reservations()
        return UseCaseResult(result, self._context, ListReservationsVerification)
