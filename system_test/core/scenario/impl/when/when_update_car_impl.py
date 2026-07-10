from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenUpdateCarImpl(BaseWhenStepImpl[None, VoidVerification]):
    """When step: update an existing car.

    Example
    -------
    scenario.when().update_car().car_id("car1").with_name("Updated")
        .then().should_succeed()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().update_car()

    def car_id(self, alias: str) -> "WhenUpdateCarImpl":
        self._use_case.car_id(alias)
        return self

    def with_name(self, value: str) -> "WhenUpdateCarImpl":
        self._use_case.name(value)
        return self

    def with_connector_types(self, value: list) -> "WhenUpdateCarImpl":
        self._use_case.connector_types(value)
        return self

    def with_battery_charge_limit(self, value: int) -> "WhenUpdateCarImpl":
        self._use_case.battery_charge_limit(value)
        return self

    def with_battery_size(self, value: int) -> "WhenUpdateCarImpl":
        self._use_case.battery_size(value)
        return self

    def with_max_kw_ac(self, value: int) -> "WhenUpdateCarImpl":
        self._use_case.max_kw_ac(value)
        return self

    def with_max_kw_dc(self, value: int) -> "WhenUpdateCarImpl":
        self._use_case.max_kw_dc(value)
        return self

    def _execute(self) -> UseCaseResult[None, VoidVerification]:
        return self._use_case.execute()
