import pytest
from playwright.sync_api import Page
from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.system.reservation_system.ui.system_ui_driver import SystemUiDriver
from system_test.core.drivers.system.reservation_system.api.system_api_driver import SystemApiDriver
from system_test.core.matchers.result_matchers import to_be_success

@pytest.fixture
def system_api_driver() -> SystemApiDriver :
    return DriverFactory.create_system_api_driver()


@pytest.fixture
def system_ui_driver(page: Page) -> SystemUiDriver:
    return DriverFactory.create_system_ui_driver(page)

@pytest.fixture
def authenticated_api_driver(system_api_driver: SystemApiDriver) -> SystemApiDriver:
    result = system_api_driver.login("addisonw", "addisonwpass")
    to_be_success(result)
    return system_api_driver

@pytest.fixture
def authenticated_ui_driver(system_ui_driver: SystemUiDriver) -> SystemUiDriver:
    result = system_ui_driver.login("addisonw", "addisonwpass")
    to_be_success(result)
    return system_ui_driver