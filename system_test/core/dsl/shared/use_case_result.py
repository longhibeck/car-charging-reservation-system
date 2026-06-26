from collections.abc import Callable

from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.dsl.shared.error_verification import ErrorVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext


class UseCaseResult[R, V]:
    """Returned by every use-case execute().

    Owns the single assertion point:
    - should_succeed() → asserts success, passes the unwrapped value to the
                         domain-specific Verification factory, returns V.
    - should_fail()    → asserts failure, returns ErrorVerification for
                         further error-message assertions.
    """

    def __init__(
        self,
        result: Result[R],
        context: UseCaseContext,
        success_verification_factory: Callable[[R, UseCaseContext], V],
    ) -> None:
        self._result = result
        self._context = context
        self._success_verification_factory = success_verification_factory

    def should_succeed(self) -> V:
        ResultAssert.assert_that_result(self._result).is_success()
        return self._success_verification_factory(
            self._result.get_value(), self._context
        )

    def should_fail(self) -> ErrorVerification:
        ResultAssert.assert_that_result(self._result).is_failure()
        return ErrorVerification(self._result.get_error_messages(), self._context)
