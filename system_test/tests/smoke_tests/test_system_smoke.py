"""
System smoke tests.

Mirrors MyShopSmokeTest from mod06: a single class with @channel(API, UI)
instead of separate TestSystemApiSmoke / TestSystemUiSmoke classes.
"""

import pytest

from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.core.use_case_dsl import UseCaseDsl


class TestSystemSmoke:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = UseCaseDsl()
        yield
        self.app.close()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_go_to_system(self):
        self.app.system().go_to_system().execute().should_succeed()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_login(self):
        (
            self.app.system()
            .login()
            .username("addisonw")
            .password("addisonwpass")
            .execute()
            .should_succeed()
        )

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_list_cars(self):
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().list_cars().execute().should_succeed()
