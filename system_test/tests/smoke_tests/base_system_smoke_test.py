import pytest

from abc import ABC, abstractmethod


class BaseSmokeTest(ABC):
    @abstractmethod
    def create_driver(self): ...

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = self.create_driver()
        yield
        self.driver.close()
