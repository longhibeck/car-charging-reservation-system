from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.tests.smoke_tests.base_system_smoke_test import BaseSmokeTest
from system_test.core.drivers.driver_factory import DriverFactory


class TestSystemApiSmoke(BaseSmokeTest):
    def create_driver(self):
        return DriverFactory.create_system_api_driver()

    def test_should_be_able_to_list_reservations(self):
        result_login = self.driver.login("addisonw", "addisonwpass")
        ResultAssert.assert_that_result(result_login).is_success()
        result = self.driver.list_reservations()
        ResultAssert.assert_that_result(result).is_success()
