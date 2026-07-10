from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.system.add_car import AddCarResponse, AddCarVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenAddCarImpl(BaseWhenStepImpl[AddCarResponse, AddCarVerification]):
    """When step: add a new car.

    Example
    -------
    scenario.when().add_car().car_id("car1").with_name("Tesla")
        .then().should_succeed().has_name("Tesla")
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().add_car()

    def car_id(self, alias: str) -> "WhenAddCarImpl":
        self._use_case.car_id(alias)
        return self

    def with_name(self, value: str) -> "WhenAddCarImpl":
        self._use_case.name(value)
        return self

    def with_connector_types(self, value: list) -> "WhenAddCarImpl":
        self._use_case.connector_types(value)
        return self

    def with_battery_charge_limit(self, value: int) -> "WhenAddCarImpl":
        self._use_case.battery_charge_limit(value)
        return self

    def with_battery_size(self, value: int) -> "WhenAddCarImpl":
        self._use_case.battery_size(value)
        return self

    def with_max_kw_ac(self, value: int) -> "WhenAddCarImpl":
        self._use_case.max_kw_ac(value)
        return self

    def with_max_kw_dc(self, value: int) -> "WhenAddCarImpl":
        self._use_case.max_kw_dc(value)
        return self

    def _execute(self) -> UseCaseResult[AddCarResponse, AddCarVerification]:
        return self._use_case.execute()
