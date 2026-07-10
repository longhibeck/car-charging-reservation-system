from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_scenario_dsl_test import BaseScenarioDslTest


class TestAuthApiSmoke(BaseScenarioDslTest):
    @channel(ChannelType.API)
    def test_should_go_to_auth(self):
        self.scenario().assume().auth().should_be_running()
