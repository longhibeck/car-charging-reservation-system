from system_test.core.dsl.shared.error_verification import ErrorVerification
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class ThenResultStageImpl[R, V]:
    """Concrete ThenResultStage returned by every WhenStep.then().

    Forces the caller to first choose should_succeed() or should_fail()
    before making domain assertions — matching the port contract exactly.

    Example
    -------
    scenario.when().add_car().then().should_succeed().has_name("Tesla")
    scenario.when().login().username("x").password("y")
        .then().should_fail().error_message("Invalid credentials")
    """

    def __init__(self, result: UseCaseResult[R, V]) -> None:
        self._result = result

    def should_succeed(self) -> V:
        return self._result.should_succeed()

    def should_fail(self) -> ErrorVerification:
        return self._result.should_fail()

    # ------------------------------------------------------------------
    # ThenStage navigation — expanded in later steps; stubs here
    # ------------------------------------------------------------------

    def reservation(self, alias: str) -> object:
        raise NotImplementedError(
            "reservation() navigation not yet implemented on ThenResultStageImpl"
        )

    def car(self, alias: str) -> object:
        raise NotImplementedError(
            "car() navigation not yet implemented on ThenResultStageImpl"
        )
