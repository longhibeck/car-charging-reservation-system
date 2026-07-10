from system_test.core.scenario.port.assume.assume_stage import AssumeStage
from system_test.core.scenario.port.assume.steps.assume_running import AssumeRunning
from system_test.core.use_case_dsl import UseCaseDsl


class AssumeRunningImpl:
    """Concrete AssumeRunning: runs a single reachability check and returns
    back to AssumeStage so further checks can be chained.

    Example
    -------
    scenario.assume().system().should_be_running()
    scenario.assume().system().should_be_running().auth().should_be_running()
    """

    def __init__(self, check_fn, assume_stage: AssumeStage) -> None:
        self._check_fn = check_fn
        self._assume_stage = assume_stage

    def should_be_running(self) -> AssumeStage:
        self._check_fn()
        return self._assume_stage


class AssumeImpl:
    """Concrete AssumeStage: delegates each check to the corresponding
    go_to_*().execute().should_succeed() call on the Use Case DSL.

    Example
    -------
    scenario.assume().system().should_be_running()
    scenario.assume().auth().should_be_running()
    scenario.assume().charging_points().should_be_running()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        self._app = app

    def system(self) -> AssumeRunning:
        return AssumeRunningImpl(
            lambda: self._app.system().go_to_system().execute().should_succeed(),
            self,
        )

    def auth(self) -> AssumeRunning:
        return AssumeRunningImpl(
            lambda: self._app.auth().go_to_auth().execute().should_succeed(),
            self,
        )

    def charging_points(self) -> AssumeRunning:
        return AssumeRunningImpl(
            lambda: (
                self._app.charging_points()
                .go_to_charging_points()
                .execute()
                .should_succeed()
            ),
            self,
        )
