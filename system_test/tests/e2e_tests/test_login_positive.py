from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_e2e_test import BaseE2eTest


class TestLoginPositive(BaseE2eTest):
    @channel(ChannelType.API, ChannelType.UI)
    def test_should_login(self):
        (
            self.scenario.when()
            .login()
            .username("addisonw")
            .password("addisonwpass")
            .then()
            .should_succeed()
            .has_access_token()
        )
