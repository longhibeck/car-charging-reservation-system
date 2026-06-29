from system_test.core.drivers.system.commons.dtos.car_request import AddCarRequest
from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.base_use_case import BaseUseCase
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
        assert sorted(self._response["connector_types"]) == sorted(expected), (
            f"Expected connector types {sorted(expected)} but got {sorted(self._response['connector_types'])}"
        )
        return self

    def has_valid_id(self) -> "AddCarVerification":
        assert self._response["id"], (
            f"Expected a non-empty id but got '{self._response['id']}'"
        )
        return self

    def has_battery_charge_limit(self, expected: int) -> "AddCarVerification":
        assert self._response["battery_charge_limit"] == expected, (
            f"Expected battery_charge_limit {expected} but got {self._response['battery_charge_limit']}"
        )
        return self

    def has_battery_size(self, expected: int) -> "AddCarVerification":
        assert self._response["battery_size"] == expected, (
            f"Expected battery_size {expected} but got {self._response['battery_size']}"
        )
        return self


class AddCar(BaseUseCase[SystemDriver, AddCarResponse, AddCarVerification]):
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
        super().__init__(driver, context)
        self._car_id_alias: str | None = None
        self._name: str = "Test Car"
        self._connector_types: list = ["CCS"]
        self._battery_charge_limit: int = 80
        self._battery_size: int = 60
        self._max_kw_ac: int = 11
        self._max_kw_dc: int = 100

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
            name=self._name,
            connector_types=self._connector_types,
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
