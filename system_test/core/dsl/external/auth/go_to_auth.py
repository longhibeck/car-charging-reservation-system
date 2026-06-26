from system_test.core.drivers.external.auth.auth_driver import AuthDriver
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification


class GoToAuth:
    """Use case: check the auth service is reachable.

    Example
    -------
    app.auth().go_to_auth().execute().should_succeed()
    """

    def __init__(self, driver: AuthDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def execute(self) -> UseCaseResult[None, VoidVerification]:
        result = self._driver.go_to_auth()
        return UseCaseResult(result, self._context, VoidVerification)
