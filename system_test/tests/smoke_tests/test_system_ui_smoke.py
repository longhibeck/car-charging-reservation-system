from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.tests.smoke_tests.base_system_smoke_test import (
    BaseSmokeTest,
)
from system_test.core.drivers.driver_factory import DriverFactory


class TestSystemUiSmoke(BaseSmokeTest):
    def create_driver(self):
        return DriverFactory.create_system_ui_driver()

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
