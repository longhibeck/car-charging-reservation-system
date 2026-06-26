from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class ListCarsVerification(ResponseVerification[list[AddCarResponse]]):
    """Assertions on a list-cars result.

    Example
    -------
    .execute().should_succeed().is_not_empty()
    """

    def is_not_empty(self) -> "ListCarsVerification":
        assert self._response, "Expected at least one car but the list was empty"
        return self

    def has_count(self, expected: int) -> "ListCarsVerification":
        assert len(self._response) == expected, (
            f"Expected {expected} cars but got {len(self._response)}"
        )
        return self


class ListCars(BaseUseCase[SystemDriver, list[AddCarResponse], ListCarsVerification]):
    """Use case: retrieve the list of cars for the current user.

    Example
    -------
    app.system().list_cars().execute().should_succeed()
    """

    def execute(self) -> UseCaseResult[list[AddCarResponse], ListCarsVerification]:
        result = self._driver.list_cars()
        return UseCaseResult(result, self._context, ListCarsVerification)
