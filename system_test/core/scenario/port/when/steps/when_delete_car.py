from typing import Protocol

from system_test.core.scenario.port.when.steps.when_step import WhenStep


class WhenDeleteCar(WhenStep[object, object], Protocol):
    def car_id(self, alias: str) -> WhenDeleteCar: ...
