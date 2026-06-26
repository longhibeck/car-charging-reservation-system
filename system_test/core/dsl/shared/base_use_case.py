from abc import ABC, abstractmethod

from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class BaseUseCase[D, R, V](ABC):
    """Abstract base class for all use cases.

    Holds the driver and the shared context.  Declares execute() as abstract
    so every subclass is forced to implement it, making R and V genuinely used.
    """

    def __init__(self, driver: D, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    @abstractmethod
    def execute(self) -> UseCaseResult[R, V]: ...
