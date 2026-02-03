import pytest
from system_test.core.drivers.driver_factory import DriverFactory


@pytest.fixture()
def auth_api_driver():
    return DriverFactory.create_auth_api_driver()


@pytest.fixture()
def charging_points_api_driver():
    return DriverFactory.create_charging_points_api_driver()