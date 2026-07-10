from uuid import uuid4

from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.tests.base.base_e2e_test import BaseE2eTest


class TestReservationNegative(BaseE2eTest):
    @channel(ChannelType.API)
    def test_should_not_create_reservation_with_not_existent_car(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .when()
            .create_reservation()
            .car_id(str(uuid4()))
            .charging_point_id(str(uuid4()))
            .then()
            .should_fail()
            .error_message("Car not found")
        )

    @channel(ChannelType.API)
    def test_should_not_create_reservation_with_not_existent_charging_point(self):
        (
            self.scenario.given()
            .user_is_logged_in()
            .car("car1")
            .exists()
            .when()
            .create_reservation()
            .car_id("car1")
            .charging_point_id(str(uuid4()))
            .then()
            .should_fail()
            .error_message(
                "Charging point is not available during the requested time. Charging point not found"
            )
        )
