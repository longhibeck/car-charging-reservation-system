from system_test.tests.e2e_tests.test_base_e2e import BaseE2eTest
from system_test.core.drivers.driver_factory import DriverFactory

class TestUiE2e(BaseE2eTest):

    def create_system_driver(self):
        return DriverFactory.create_system_ui_driver()