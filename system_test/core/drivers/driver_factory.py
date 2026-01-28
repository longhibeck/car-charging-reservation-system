from system_test.core.system_test_configuration import SystemTestConfiguration
from system_test.core.drivers.system.reservation_system.api.system_api_driver import SystemApiDriver
from system_test.core.drivers.system.reservation_system.ui.system_ui_driver import SystemUiDriver
from playwright.sync_api import Page


class DriverFactory:

    @staticmethod
    def create_system_ui_driver(page: Page):
        return SystemUiDriver(page, SystemTestConfiguration.get_car_charging_reservation_ui_base_url())
            
    @staticmethod
    def create_system_api_driver():
        return SystemApiDriver(SystemTestConfiguration.get_car_charging_reservation_api_base_url())