from typing import Protocol, TypeVar

from system_test.core.scenario.port.then.then_result_stage import ThenResultStage

R = TypeVar("R")
V = TypeVar("V")


class WhenStep(Protocol[R, V]):
    """Base port for executable action steps."""

    def then(self) -> ThenResultStage[R, V]: ...
