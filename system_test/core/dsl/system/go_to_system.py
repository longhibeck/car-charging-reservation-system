from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.dsl.shared.void_verification import VoidVerification


class GoToSystem(BaseUseCase[SystemDriver, None, VoidVerification]):
    """Use case: navigate to / check the system is reachable.

    Returns a void result — the only useful assertion is should_succeed().

    Example
    -------
    app.system().go_to_system().execute().should_succeed()
    """

    def execute(self) -> UseCaseResult[None, VoidVerification]:
        result = self._driver.go_to_system()
        return UseCaseResult(result, self._context, VoidVerification)
