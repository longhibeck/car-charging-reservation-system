from system_test.core.drivers.system.commons.dtos.car_request import AddCarRequest
from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class AddCarVerification(ResponseVerification[AddCarResponse]):
    """Assertions on an add-car result.

    Example
    -------
    .execute().should_succeed().has_name("BYD Seal U")
    """

    def has_name(self, expected: str) -> "AddCarVerification":
        assert self._response["name"] == expected, (
            f"Expected car name '{expected}' but got '{self._response['name']}'"
        )
        return self

    def has_connector_types(self, expected: list) -> "AddCarVerification":
        assert self._response["connector_types"] == expected, (
            f"Expected connector types {expected} but got {self._response['connector_types']}"
        )
        return self


class AddCar:
    """Use case: add a new car for the current user.

    The optional car_id() setter names a result alias under which the
    created car's ID is stored in the context for use by subsequent
    use cases (e.g. CreateReservation, UpdateCar, DeleteCar).

    Example
    -------
    app.system().add_car().car_id("car1").name("BYD Seal U")
        .connector_types(["CCS"]).battery_charge_limit(100)
        .battery_size(87).max_kw_ac(11).max_kw_dc(15)
        .execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context
        self._car_id_alias: str | None = None
        self._name: str | None = None
        self._connector_types: list | None = None
        self._battery_charge_limit: int | None = None
        self._battery_size = None
        self._max_kw_ac: int | None = None
        self._max_kw_dc: int | None = None

    def car_id(self, alias: str) -> "AddCar":
        """Result alias under which the created car ID is stored."""
        self._car_id_alias = alias
        return self

    def name(self, value: str) -> "AddCar":
        self._name = value
        return self

    def connector_types(self, value: list) -> "AddCar":
        self._connector_types = value
        return self

    def battery_charge_limit(self, value: int) -> "AddCar":
        self._battery_charge_limit = value
        return self

    def battery_size(self, value) -> "AddCar":
        self._battery_size = value
        return self

    def max_kw_ac(self, value: int) -> "AddCar":
        self._max_kw_ac = value
        return self

    def max_kw_dc(self, value: int) -> "AddCar":
        self._max_kw_dc = value
        return self

    def execute(self) -> UseCaseResult[AddCarResponse, AddCarVerification]:
        request = AddCarRequest(
            name=self._name or "",
            connector_types=self._connector_types or [],
            battery_charge_limit=self._battery_charge_limit,
            battery_size=self._battery_size,
            max_kw_ac=self._max_kw_ac,
            max_kw_dc=self._max_kw_dc,
        )
        result = self._driver.add_car(request)

        if self._car_id_alias is not None:
            if result.is_success():
                self._context.set_result_entry(
                    self._car_id_alias, str(result.get_value()["id"])
                )
            else:
                self._context.set_result_entry_failed(
                    self._car_id_alias, str(result.get_error_messages())
                )

        return UseCaseResult(result, self._context, AddCarVerification)
