from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_scenario_dsl_test import BaseScenarioDslTest


class TestChargingPointsApiSmoke(BaseScenarioDslTest):
    @channel(ChannelType.API)
    def test_should_go_to_charging_points(self):
        self.scenario().assume().charging_points().should_be_running()
