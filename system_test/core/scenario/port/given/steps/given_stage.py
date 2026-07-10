from typing import TYPE_CHECKING, Protocol

from system_test.core.scenario.port.given.steps.given_car import GivenCar
from system_test.core.scenario.port.given.steps.given_reservation import (
    GivenReservation,
)

if TYPE_CHECKING:
    from system_test.core.scenario.port.then.then_stage import ThenStage
    from system_test.core.scenario.port.when.when_stage import WhenStage


class GivenStage(Protocol):
    def user_is_logged_in(
        self,
        username: str = "addisonw",
        password: str = "addisonwpass",
    ) -> "GivenStage": ...

    def car(self, alias: str) -> GivenCar: ...

    def reservation(self, alias: str) -> GivenReservation: ...

    def when(self) -> "WhenStage": ...

    def then(self) -> "ThenStage": ...
