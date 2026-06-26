from system_test.core.drivers.system.commons.dtos.car_request import UpdateCarRequest
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification


class UpdateCar(BaseUseCase[SystemDriver, None, VoidVerification]):
    """Use case: update an existing car.

    car_id() resolves from the context result map — pass the same alias
    used in the preceding add_car() call.

    Example
    -------
    app.system().update_car().car_id("car1").name("Tesla Updated")
        .connector_types(["CCS", "Type 2"]).battery_charge_limit(95)
        .battery_size(80).max_kw_ac(22).max_kw_dc(300)
        .execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        super().__init__(driver, context)
        self._car_id_alias: str | None = None
        self._name: str | None = None
        self._connector_types: list | None = None
        self._battery_charge_limit: int | None = None
        self._battery_size: int | None = None
        self._max_kw_ac: int | None = None
        self._max_kw_dc: int | None = None

    def car_id(self, alias: str) -> "UpdateCar":
        self._car_id_alias = alias
        return self

    def name(self, value: str) -> "UpdateCar":
        self._name = value
        return self

    def connector_types(self, value: list) -> "UpdateCar":
        self._connector_types = value
        return self

    def battery_charge_limit(self, value: int) -> "UpdateCar":
        self._battery_charge_limit = value
        return self

    def battery_size(self, value: int) -> "UpdateCar":
        self._battery_size = value
        return self

    def max_kw_ac(self, value: int) -> "UpdateCar":
        self._max_kw_ac = value
        return self

    def max_kw_dc(self, value: int) -> "UpdateCar":
        self._max_kw_dc = value
        return self

    def execute(self) -> UseCaseResult[None, VoidVerification]:
        car_id = self._context.get_result_value(self._car_id_alias)
        request = UpdateCarRequest(
            name=self._name or "",
            connector_types=self._connector_types or [],
            battery_charge_limit=self._battery_charge_limit,
            battery_size=self._battery_size,
            max_kw_ac=self._max_kw_ac,
            max_kw_dc=self._max_kw_dc,
        )
        result = self._driver.update_car(car_id, request)
        return UseCaseResult(result, self._context, VoidVerification)
