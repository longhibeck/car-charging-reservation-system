import pytest

from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_e2e_test import BaseE2eTest


class TestCarPositive(BaseE2eTest):
    @channel(ChannelType.API, ChannelType.UI)
    def test_should_add_car(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .when()
            .add_car()
            .then()
            .should_succeed()
            .has_valid_id()
            .has_name("Test Car")
            .has_connector_types(["CCS"])
        )

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_list_cars(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .car("car1")
            .exists()
            .when()
            .list_cars()
            .then()
            .should_succeed()
            .is_not_empty()
        )

    @channel(ChannelType.API, ChannelType.UI)
    @pytest.mark.parametrize(
        "connector_types",
        [
            ["Type 2", "Schuko"],
            ["Type 2", "CCS"],
            ["Type 2", "CCS", "Schuko"],
        ],
    )
    def test_should_add_car_with_multiple_valid_connector_types(self, connector_types):
        (
            self.scenario.given()
            .user_is_logged_in()
            .when()
            .add_car()
            .with_connector_types(connector_types)
            .then()
            .should_succeed()
            .has_connector_types(connector_types)
        )

    @channel(ChannelType.API)
    def test_should_update_car_successfully(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .car("car1")
            .exists()
            .when()
            .update_car()
            .car_id("car1")
            .with_name("Tesla Model 3 Updated")
            .then()
            .should_succeed()
        )

    @channel(ChannelType.API)
    def test_should_delete_car_successfully(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .car("car1")
            .exists()
            .when()
            .delete_car()
            .car_id("car1")
            .then()
            .should_succeed()
        )
