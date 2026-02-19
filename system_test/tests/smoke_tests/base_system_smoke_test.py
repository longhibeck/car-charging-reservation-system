import pytest
from system_test.core.drivers.commons.result_assert import ResultAssert
from abc import ABC, abstractmethod


class BaseSmokeTest(ABC):
    @abstractmethod
    def create_driver(self): ...

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = self.create_driver()
        yield
        self.driver.close()

    def test_should_be_able_to_go_to_system(self):
        result = self.driver.go_to_system()
        ResultAssert.assert_that_result(result).is_success()

    def test_should_be_able_to_login(self):
        result = self.driver.login("addisonw", "addisonwpass")
        ResultAssert.assert_that_result(result).is_success()

    def test_should_be_able_to_list_cars(self):
        result_login = self.driver.login("addisonw", "addisonwpass")
        ResultAssert.assert_that_result(result_login).is_success()
        result = self.driver.list_cars()
        ResultAssert.assert_that_result(result).is_success()
