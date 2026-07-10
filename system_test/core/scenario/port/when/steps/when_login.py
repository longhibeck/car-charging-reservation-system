from typing import Protocol

from system_test.core.scenario.port.when.steps.when_step import WhenStep


class WhenLogin(WhenStep[object, object], Protocol):
    def username(self, value: str) -> WhenLogin: ...

    def password(self, value: str) -> WhenLogin: ...
