from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.system.go_to_system import GoToSystem
from system_test.core.dsl.system.login import Login


class SystemDsl:
    """Domain DSL for the car-charging reservation system.

    One factory method per use case — no logic here, only creation.

    Example
    -------
    app.system().go_to_system().execute().should_succeed()
    app.system().login().username("addisonw").password("pass").execute().should_succeed()
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def go_to_system(self) -> GoToSystem:
        return GoToSystem(self._driver, self._context)

    def login(self) -> Login:
        return Login(self._driver, self._context)
