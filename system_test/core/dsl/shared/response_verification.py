from system_test.core.dsl.shared.use_case_context import UseCaseContext


class ResponseVerification[R]:
    """Base class for every domain *Verification type.

    Receives the already-unwrapped success value (not the raw Result), keeping
    the contract simple: if you hold a ResponseVerification the operation
    already succeeded.

    Subclasses add domain-specific assertion helpers and access the response
    via self._response and the context via self._context.
    """

    def __init__(self, response: R, context: UseCaseContext) -> None:
        self._response = response
        self._context = context
