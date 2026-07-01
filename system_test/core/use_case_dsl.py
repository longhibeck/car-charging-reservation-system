from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.external.auth.auth_driver import AuthDriver
from system_test.core.drivers.external.charging_points.charging_points_driver import (
    ChargingPointsDriver,
)
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.external.auth.auth_dsl import AuthDsl
from system_test.core.dsl.external.charging_points.charging_points_dsl import (
    ChargingPointsDsl,
)
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
    self.app.auth().go_to_auth().execute().should_succeed()
    self.app.charging_points().go_to_charging_points().execute().should_succeed()
    """

    def __init__(self) -> None:
        self._context = UseCaseContext()
        self._system_driver: SystemDriver | None = None
        self._system_dsl: SystemDsl | None = None
        self._auth_driver: AuthDriver | None = None
        self._auth_dsl: AuthDsl | None = None
        self._charging_points_driver: ChargingPointsDriver | None = None
        self._charging_points_dsl: ChargingPointsDsl | None = None

    def system(self) -> SystemDsl:
        if self._system_dsl is None:
            self._system_driver = (
                DriverFactory.create_system_driver_for_current_channel()
            )
            self._system_dsl = SystemDsl(self._system_driver, self._context)
        return self._system_dsl

    def auth(self) -> AuthDsl:
        if self._auth_dsl is None:
            self._auth_driver = DriverFactory.create_auth_api_driver()
            self._auth_dsl = AuthDsl(self._auth_driver, self._context)
        return self._auth_dsl

    def charging_points(self) -> ChargingPointsDsl:
        if self._charging_points_dsl is None:
            self._charging_points_driver = (
                DriverFactory.create_charging_points_api_driver()
            )
            self._charging_points_dsl = ChargingPointsDsl(
                self._charging_points_driver, self._context
            )
        return self._charging_points_dsl

    def close(self) -> None:
        if self._system_driver is not None:
            self._system_driver.close()
        if self._auth_dsl is not None:
            self._auth_dsl.close()
        if self._charging_points_dsl is not None:
            self._charging_points_dsl.close()
