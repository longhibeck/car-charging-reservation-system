from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.system.login import LoginResponse, LoginVerification
from system_test.core.scenario.impl.when.base_when_step_impl import BaseWhenStepImpl
from system_test.core.use_case_dsl import UseCaseDsl


class WhenLoginImpl(BaseWhenStepImpl[LoginResponse, LoginVerification]):
    """When step: authenticate a user.

    Example
    -------
    scenario.when().login().username("addisonw").password("pass")
        .then().should_succeed().has_access_token()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        super().__init__(app)
        self._use_case = app.system().login()

    def username(self, value: str) -> "WhenLoginImpl":
        self._use_case.username(value)
        return self

    def password(self, value: str) -> "WhenLoginImpl":
        self._use_case.password(value)
        return self

    def _execute(self) -> UseCaseResult[LoginResponse, LoginVerification]:
        return self._use_case.execute()
