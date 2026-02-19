from system_test.tests.smoke_tests.base_system_smoke_test import (
    BaseSmokeTest,
)
from system_test.core.drivers.driver_factory import DriverFactory


class TestSystemUiSmoke(BaseSmokeTest):
    def create_driver(self):
        return DriverFactory.create_system_ui_driver()
