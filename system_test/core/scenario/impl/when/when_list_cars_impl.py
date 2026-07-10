from system_test.core.drivers.system.commons.dtos.car_response import AddCarResponse
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.system.list_cars import ListCarsVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenListCarsImpl(BaseWhenStepImpl[list[AddCarResponse], ListCarsVerification]):
    """When step: list all cars for the authenticated user.

    Example
    -------
    scenario.when().list_cars().then().should_succeed().is_not_empty()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().list_cars()

    def _execute(self) -> UseCaseResult[list[AddCarResponse], ListCarsVerification]:
        return self._use_case.execute()
