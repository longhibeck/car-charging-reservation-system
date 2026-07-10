from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from system_test.core.scenario.port.assume.assume_stage import AssumeStage
    from system_test.core.scenario.port.given.given_stage import GivenStage
    from system_test.core.scenario.port.when.when_stage import WhenStage


class ScenarioDsl(Protocol):
    """Top-level Scenario DSL port.

    Only stage transitions are exposed here. Implementations provide
    concrete runtime behavior later.
    """

    def assume(self) -> AssumeStage: ...

    def given(self) -> GivenStage: ...

    def when(self) -> WhenStage: ...
