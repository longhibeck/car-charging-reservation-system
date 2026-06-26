from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification


class GoToSystem:
    """Use case: navigate to / check the system is reachable.

    Returns a void result — the only useful assertion is should_succeed().

    Example
    -------
    app.system().go_to_system().execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def execute(self) -> UseCaseResult[None, VoidVerification]:
        result = self._driver.go_to_system()
        return UseCaseResult(result, self._context, VoidVerification)
