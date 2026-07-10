from typing import Protocol

from system_test.core.scenario.port.assume.steps.assume_running import AssumeRunning


class AssumeStage(Protocol):
    """Assume stage port (mirrors reference structure: assume/AssumeStage)."""

    def system(self) -> AssumeRunning: ...

    def auth(self) -> AssumeRunning: ...

    def charging_points(self) -> AssumeRunning: ...
