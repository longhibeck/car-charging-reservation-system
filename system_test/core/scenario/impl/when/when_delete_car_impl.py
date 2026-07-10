from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenDeleteCarImpl(BaseWhenStepImpl[None, VoidVerification]):
    """When step: delete an existing car.

    Example
    -------
    scenario.when().delete_car().car_id("car1").then().should_succeed()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().delete_car()

    def car_id(self, alias: str) -> "WhenDeleteCarImpl":
        self._use_case.car_id(alias)
        return self

    def _execute(self) -> UseCaseResult[None, VoidVerification]:
        return self._use_case.execute()
