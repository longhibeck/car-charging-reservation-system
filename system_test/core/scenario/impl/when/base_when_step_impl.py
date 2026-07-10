from system_test.core.dsl.shared.use_case_result import UseCaseResult
from system_test.core.scenario.impl.then.then_result_stage_impl import (
    ThenResultStageImpl,
)
from system_test.core.use_case_dsl import UseCaseDsl


class BaseWhenStepImpl[R, V]:
    """Base for every concrete WhenStep implementation.

    Subclasses store the UseCaseDsl reference and any fluent fields, then
    override _execute() to run the underlying use case and return a result.
    then() calls _execute() and wraps the result in ThenResultStageImpl,
    which enforces should_succeed()/should_fail() before domain assertions.

    Example
    -------
    scenario.when().login().username("addisonw").password("pass")
        .then().should_succeed().has_access_token()
    """

    def __init__(self, app: UseCaseDsl) -> None:
        self._app = app

    def _execute(self) -> UseCaseResult[R, V]:  # pragma: no cover
        raise NotImplementedError

    def then(self) -> ThenResultStageImpl[R, V]:
        return ThenResultStageImpl(self._execute())
