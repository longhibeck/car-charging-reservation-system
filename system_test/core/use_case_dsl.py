from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.system.system_dsl import SystemDsl


class UseCaseDsl:
    """Entry point for the Use-Case DSL.

    Lazily creates domain DSLs and their underlying drivers on first access,
    reusing the same instance for the lifetime of a test.

    Usage in a test fixture
    -----------------------
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = UseCaseDsl()
        yield
        self.app.close()

    Test body
    ---------
    self.app.system().go_to_system().execute().should_succeed()
    self.app.system().login().username("addisonw").password("pass").execute().should_succeed()
    """

    def __init__(self) -> None:
        self._context = UseCaseContext()
        self._system_driver: SystemDriver | None = None
        self._system_dsl: SystemDsl | None = None

    def system(self) -> SystemDsl:
        if self._system_dsl is None:
            self._system_driver = (
                DriverFactory.create_system_driver_for_current_channel()
            )
            self._system_dsl = SystemDsl(self._system_driver, self._context)
        return self._system_dsl

    def close(self) -> None:
        if self._system_driver is not None:
            self._system_driver.close()
