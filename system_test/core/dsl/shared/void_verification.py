from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext


class VoidVerification(ResponseVerification[None]):
    """Verification for use cases that return no domain payload."""

    def __init__(self, response: None, context: UseCaseContext) -> None:
        super().__init__(response, context)
