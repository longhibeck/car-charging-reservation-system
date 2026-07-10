from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_e2e_test import BaseE2eTest


class TestLoginNegative(BaseE2eTest):
    @channel(ChannelType.API, ChannelType.UI)
    def test_should_not_login_with_invalid_credentials(self):
        (
            self.scenario.when()
            .login()
            .username("invalid_user")
            .password("invalid_pass")
            .then()
            .should_fail()
            .error_message("Invalid credentials")
        )
