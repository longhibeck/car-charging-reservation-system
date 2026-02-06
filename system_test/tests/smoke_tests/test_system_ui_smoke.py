from system_test.tests.smoke_tests.base_system_smoke_test import (
    BaseSystemTest,
    login_as,
)
from system_test.core.drivers.driver_factory import DriverFactory


class TestSystemUiSmoke(BaseSystemTest):
    def create_driver(self):
        return DriverFactory.create_system_ui_driver()

    def test_should_be_able_to_go_to_system(self):
        result = self.driver.go_to_system()
        self.assert_that(result).is_success()

    def test_should_be_able_to_login(self):
        result = self.driver.login("addisonw", "addisonwpass")
        self.assert_that(result).is_success()

    @login_as()
    def test_should_be_able_to_list_cars(self):
        result = self.driver.list_cars()
        self.assert_that(result).is_success()
