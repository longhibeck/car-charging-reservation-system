from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from system_test.core.scenario.port.given.given_stage import GivenStage


class GivenReservation(Protocol):
    """Port for fluent reservation setup during given stage."""

    def for_car(self, alias: str) -> "GivenReservation": ...

    def on_charging_point(self, value: str) -> "GivenReservation": ...

    def from_time(self, value: str) -> "GivenReservation": ...

    def to_time(self, value: str) -> "GivenReservation": ...

    def exists(self) -> "GivenStage": ...
