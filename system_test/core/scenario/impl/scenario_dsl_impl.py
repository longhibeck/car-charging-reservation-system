from system_test.core.scenario.impl.assume.assume_impl import AssumeImpl
from system_test.core.scenario.impl.given.given_impl import GivenImpl
from system_test.core.scenario.impl.when.when_stage_impl import WhenStageImpl
from system_test.core.use_case_dsl import UseCaseDsl


class ScenarioDslImpl:
    """Concrete ScenarioDsl: wraps UseCaseDsl and delegates each stage.

    The executed flag prevents multiple Given-When-Then flows inside a
    single test method; call when() or given() a second time and an
    IllegalStateError is raised immediately.  assume() is exempt — it
    can be called any number of times without side effects.

    Usage
    -----
    @pytest.fixture(autouse=True)
    def setup(self):
        self.scenario = ScenarioDslImpl(UseCaseDsl())
        yield
        self.scenario.app.close()

    def test_something(self):
        self.scenario.given().user_is_logged_in().when().list_cars()
            .then().should_succeed().is_not_empty()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        self.app = app
        self._executed: bool = False

    # ------------------------------------------------------------------
    # Stage factory methods
    # ------------------------------------------------------------------

    def assume(self) -> AssumeImpl:
        return AssumeImpl(self.app)

    def given(self) -> GivenImpl:
        self._ensure_not_executed()
        return GivenImpl(self.app)

    def when(self) -> WhenStageImpl:
        self._ensure_not_executed()
        return WhenStageImpl(self.app)

    # ------------------------------------------------------------------
    # Execution guard
    # ------------------------------------------------------------------

    def mark_as_executed(self) -> None:
        self._executed = True

    def _ensure_not_executed(self) -> None:
        if self._executed:
            raise RuntimeError(
                "Scenario has already been executed. "
                "Each test method should contain only ONE scenario execution "
                "(Given-When-Then). Split multiple scenarios into separate test methods."
            )
