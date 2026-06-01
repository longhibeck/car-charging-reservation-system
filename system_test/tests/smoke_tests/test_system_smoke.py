"""
System smoke tests.

Mirrors MyShopSmokeTest from mod06: a single class with @channel(API, UI)
instead of separate TestSystemApiSmoke / TestSystemUiSmoke classes.
"""

import pytest
from system_test.channel import channel, ChannelType
from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.system.commons.dtos.auth_request import LoginRequest


class TestSystemSmoke:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = DriverFactory.create_system_driver_for_current_channel()
        yield
        self.driver.close()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_go_to_system(self):
        result = self.driver.go_to_system()
        ResultAssert.assert_that_result(result).is_success()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_login(self):
        result = self.driver.login(LoginRequest(username="addisonw", password="addisonwpass"))
        ResultAssert.assert_that_result(result).is_success()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_list_cars(self):
        result_login = self.driver.login(LoginRequest(username="addisonw", password="addisonwpass"))
        ResultAssert.assert_that_result(result_login).is_success()
        result = self.driver.list_cars()
        ResultAssert.assert_that_result(result).is_success()
