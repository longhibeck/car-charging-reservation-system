from system_test.core.drivers.system.commons.dtos.reservation_request import (
    CreateReservationRequest,
)
from system_test.core.drivers.system.commons.dtos.reservation_response import (
    ReservationResponse,
)
from system_test.core.drivers.system.commons.enums.reservation_status import (
    ReservationStatusLiteral,
)
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class CreateReservationVerification(ResponseVerification[ReservationResponse]):
    """Assertions on a create-reservation result.

    Example
    -------
    .execute().should_succeed().has_status("active")
    """

    def has_status(
        self, expected: ReservationStatusLiteral
    ) -> "CreateReservationVerification":
        assert self._response["status"] == expected, (
            f"Expected reservation status '{expected}' but got '{self._response['status']}'"
        )
        return self


class CreateReservation(
    BaseUseCase[SystemDriver, ReservationResponse, CreateReservationVerification]
):
    """Use case: create a charging reservation.

    car_id() and charging_point_id() are resolved via get_result_value(),
    so they can be either stored aliases (from a prior add_car()) or
    literal UUID strings (e.g. for negative tests).

    The optional reservation_id() setter names a result alias under which
    the created reservation's ID is stored for use by get_reservation().

    Example
    -------
    app.system().create_reservation()
        .reservation_id("res1").car_id("car1")
        .charging_point_id("550e8400-e29b-41d4-a716-446655440001")
        .start_time(start_time).end_time(end_time)
        .execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        super().__init__(driver, context)
        self._reservation_id_alias: str | None = None
        self._car_id_alias: str | None = None
        self._charging_point_id_alias: str | None = None
        self._start_time: str | None = None
        self._end_time: str | None = None

    def reservation_id(self, alias: str) -> "CreateReservation":
        """Result alias under which the created reservation ID is stored."""
        self._reservation_id_alias = alias
        return self

    def car_id(self, alias: str) -> "CreateReservation":
        self._car_id_alias = alias
        return self

    def charging_point_id(self, alias: str) -> "CreateReservation":
        self._charging_point_id_alias = alias
        return self

    def start_time(self, value: str) -> "CreateReservation":
        self._start_time = value
        return self

    def end_time(self, value: str) -> "CreateReservation":
        self._end_time = value
        return self

    def execute(
        self,
    ) -> UseCaseResult[ReservationResponse, CreateReservationVerification]:
        car_id = self._context.get_result_value(self._car_id_alias)
        charging_point_id = self._context.get_result_value(
            self._charging_point_id_alias
        )

        request = CreateReservationRequest(
            car_id=car_id,
            charging_point_id=charging_point_id,
            start_time=self._start_time or "",
            end_time=self._end_time or "",
        )
        result = self._driver.create_reservation(request)

        if self._reservation_id_alias is not None:
            if result.is_success():
                self._context.set_result_entry(
                    self._reservation_id_alias, str(result.get_value()["id"])
                )
            else:
                self._context.set_result_entry_failed(
                    self._reservation_id_alias, str(result.get_error_messages())
                )

        return UseCaseResult(result, self._context, CreateReservationVerification)
