from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from system_test.core.scenario.port.assume.assume_stage import AssumeStage


class AssumeRunning(Protocol):
    """Port for the result of an assume-system selection step."""

    def should_be_running(self) -> "AssumeStage": ...
