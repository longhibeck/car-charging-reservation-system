import pytest

from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_e2e_test import BaseE2eTest


class TestCarNegative(BaseE2eTest):
    @channel(ChannelType.API)
    def test_should_not_add_car_with_invalid_data_type(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .when()
            .add_car()
            .with_battery_size("not-a-number")
            .then()
            .should_fail()
            .error_message(
                "Input should be a valid integer, unable to parse string as an integer"
            )
        )

    @channel(ChannelType.API)
    @pytest.mark.parametrize("value", [0, -10, -20])
    def test_should_not_create_car_with_zero_or_negative_battery_charge_limit(
        self, value
    ):
        (
            self.scenario.given()
            .user_is_logged_in()
            .when()
            .add_car()
            .with_battery_charge_limit(value)
            .then()
            .should_fail()
            .error_message("Input should be greater than 0")
        )

    @channel(ChannelType.API)
    @pytest.mark.parametrize("value", [101, 200, 150])
    def test_should_not_create_car_with_over_hundred_battery_charge_limit(self, value):
        (
            self.scenario.given()
            .user_is_logged_in()
            .when()
            .add_car()
            .with_battery_charge_limit(value)
            .then()
            .should_fail()
            .error_message("Input should be less than or equal to 100")
        )
