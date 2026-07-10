from typing import Protocol, TypeVar

from system_test.core.dsl.shared.error_verification import ErrorVerification
from system_test.core.scenario.port.then.then_stage import ThenStage

V = TypeVar("V")


class ThenResultStage(ThenStage, Protocol[V]):
    """Result-aware then stage port (mirrors reference structure)."""

    def should_succeed(self) -> V: ...

    def should_fail(self) -> ErrorVerification: ...
