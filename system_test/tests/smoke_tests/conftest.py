import pytest
from playwright.sync_api import Page
from system_test.core.drivers.driver_factory import DriverFactory


@pytest.fixture
def system_api_driver():
    return DriverFactory.create_system_api_driver()


@pytest.fixture
def system_ui_driver(page: Page):
    return DriverFactory.create_system_ui_driver(page)

@pytest.fixture
def authenticated_api_driver(system_api_driver):
    """Fixture that provides an authenticated API driver"""
    from system_test.core.matchers.result_matchers import to_be_success
    
    result = system_api_driver.login("addisonw", "addisonwpass")
    to_be_success(result)  # Driver is now auto-authenticated
    
    return system_api_driver