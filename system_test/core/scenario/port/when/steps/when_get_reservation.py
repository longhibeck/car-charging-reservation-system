from typing import Protocol

from system_test.core.scenario.port.when.steps.when_step import WhenStep


class WhenGetReservation(WhenStep[object, object], Protocol):
    def reservation_id(self, alias: str) -> WhenGetReservation: ...
