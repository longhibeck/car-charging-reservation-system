import pytest

from abc import ABC, abstractmethod


class BaseSmokeTest(ABC):
    @abstractmethod
    def create_driver(self): ...

    @pytest.fixture(autouse=True)
    def setup_driver(self):
        self.driver = self.create_driver()
