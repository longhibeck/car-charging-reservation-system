from typing import Protocol

from system_test.core.scenario.port.when.steps.when_step import WhenStep


class WhenListCars(WhenStep[object, object], Protocol): ...
