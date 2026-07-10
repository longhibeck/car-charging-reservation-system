from typing import Protocol

from system_test.core.scenario.port.assume.steps.assume_running import AssumeRunning


class AssumeStage(Protocol):
    def system(self) -> AssumeRunning: ...

    def auth(self) -> AssumeRunning: ...

    def charging_points(self) -> AssumeRunning: ...
