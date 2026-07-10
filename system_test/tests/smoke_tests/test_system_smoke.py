from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_scenario_dsl_test import BaseScenarioDslTest


class TestSystemSmoke(BaseScenarioDslTest):
    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_go_to_system(self):
        self.scenario().assume().system().should_be_running()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_login(self):
        self.scenario().when().login().username("addisonw").password(
            "addisonwpass"
        ).then().should_succeed().has_access_token()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_be_able_to_list_cars(self):
        self.scenario().given().user_is_logged_in().when().list_cars().then().should_succeed()
