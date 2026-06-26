from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext


class ErrorVerification(ResponseVerification[list[str]]):
    """Verification returned by UseCaseResult.should_fail().

    Receives the list of error messages from the failed Result.
    Chain assertion helpers to check specific error content.

    Example
    -------
    .execute().should_fail().error_message("Invalid credentials")
    """

    def __init__(self, error_messages: list[str], context: UseCaseContext) -> None:
        super().__init__(error_messages, context)

    def error_message(self, expected: str) -> "ErrorVerification":
        expanded = self._context.expand_aliases(expected)
        assert expanded in self._response, (
            f"Expected error '{expanded}' but errors were: {self._response}"
        )
        return self
