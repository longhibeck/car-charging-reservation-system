from typing import Protocol


class ThenStage(Protocol):
    """Base then stage port.

    Domain-specific assertion navigation can be expanded in later steps.
    """

    def reservation(self, alias: str) -> object: ...

    def car(self, alias: str) -> object: ...
