from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_e2e_test import BaseE2eTest

CHARGING_POINT_ID = "550e8400-e29b-41d4-a716-446655440001"


class TestReservationPositive(BaseE2eTest):
    @channel(ChannelType.API)
    def test_should_list_reservations(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .when()
            .list_reservations()
            .then()
            .should_succeed()
        )

    @channel(ChannelType.API)
    def test_should_create_reservation_successfully(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .car("car1")
            .exists()
            .when()
            .create_reservation()
            .car_id("car1")
            .charging_point_id(CHARGING_POINT_ID)
            .then()
            .should_succeed()
            .has_status("active")
        )

    @channel(ChannelType.API)
    def test_should_get_reservation_successfully(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .car("car1")
            .exists()
            .reservation("res1")
            .for_car("car1")
            .on_charging_point(CHARGING_POINT_ID)
            .exists()
            .when()
            .get_reservation()
            .reservation_id("res1")
            .then()
            .should_succeed()
            .has_valid_id()
            .has_status("active")
            .has_car_id("car1")
            .has_charging_point_id(CHARGING_POINT_ID)
        )
