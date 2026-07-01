from uuid import uuid4

import pytest

from system_test.core.channels.channel_decorator import channel
from system_test.core.channels.channel_type import ChannelType
from system_test.core.use_case_dsl import UseCaseDsl

# Known charging point seeded in the test environment
CHARGING_POINT_ID = "550e8400-e29b-41d4-a716-446655440001"


class TestE2e:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = UseCaseDsl()
        yield
        self.app.close()

    # ------------------------------------------------------------------
    # Auth
    # ------------------------------------------------------------------

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_login(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed().has_access_token()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_not_login_with_invalid_credentials(self) -> None:
        (
            self.app.system()
            .login()
            .username("invalid_user")
            .password("invalid_pass")
            .execute()
            .should_fail()
            .error_message("Invalid credentials")
        )

    # ------------------------------------------------------------------
    # Cars – positive
    # ------------------------------------------------------------------

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_add_car(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().add_car().execute().should_succeed().has_valid_id().has_name(
            "Test Car"
        ).has_connector_types(["CCS"])

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_list_cars(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().add_car().execute().should_succeed()
        self.app.system().list_cars().execute().should_succeed().is_not_empty()

    @channel(ChannelType.API, ChannelType.UI)
    @pytest.mark.parametrize(
        "connector_types",
        [
            ["Type 2", "Schuko"],
            ["Type 2", "CCS"],
            ["Type 2", "CCS", "Schuko"],
        ],
    )
    def test_should_add_car_with_multiple_valid_connector_types(
        self, connector_types
    ) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        (
            self.app.system()
            .add_car()
            .connector_types(connector_types)
            .execute()
            .should_succeed()
            .has_connector_types(connector_types)
        )

    @channel(ChannelType.API)
    def test_should_update_car_successfully(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().add_car().car_id("car1").execute().should_succeed()
        self.app.system().update_car().car_id("car1").name(
            "Tesla Model 3 Updated"
        ).execute().should_succeed()

    @channel(ChannelType.API)
    def test_should_delete_car_successfully(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().add_car().car_id("car1").execute().should_succeed()
        self.app.system().delete_car().car_id("car1").execute().should_succeed()

    # ------------------------------------------------------------------
    # Cars – negative
    # ------------------------------------------------------------------

    @channel(ChannelType.API)
    def test_should_not_add_car_with_invalid_data_type(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        (
            self.app.system()
            .add_car()
            .battery_size("not-a-number")
            .execute()
            .should_fail()
            .error_message(
                "Input should be a valid integer, unable to parse string as an integer"
            )
        )

    @channel(ChannelType.API)
    @pytest.mark.parametrize("value", [0, -10, -20])
    def test_should_not_create_car_with_zero_or_negative_battery_charge_limit(
        self, value
    ) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        (
            self.app.system()
            .add_car()
            .battery_charge_limit(value)
            .execute()
            .should_fail()
            .error_message("Input should be greater than 0")
        )

    @channel(ChannelType.API)
    @pytest.mark.parametrize("value", [101, 200, 150])
    def test_should_not_create_car_with_over_hundred_battery_charge_limit(
        self, value
    ) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        (
            self.app.system()
            .add_car()
            .battery_charge_limit(value)
            .execute()
            .should_fail()
            .error_message("Input should be less than or equal to 100")
        )

    # ------------------------------------------------------------------
    # Reservations – positive
    # ------------------------------------------------------------------

    @channel(ChannelType.API)
    def test_should_list_reservations(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().list_reservations().execute().should_succeed()

    @channel(ChannelType.API)
    def test_should_create_reservation_successfully(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().add_car().car_id("car1").execute().should_succeed()
        (
            self.app.system()
            .create_reservation()
            .car_id("car1")
            .charging_point_id(CHARGING_POINT_ID)
            .execute()
            .should_succeed()
            .has_status("active")
        )

    @channel(ChannelType.API)
    def test_should_get_reservation_successfully(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().add_car().car_id("car1").execute().should_succeed()
        (
            self.app.system()
            .create_reservation()
            .reservation_id("res1")
            .car_id("car1")
            .charging_point_id(CHARGING_POINT_ID)
            .execute()
            .should_succeed()
            .has_status("active")
        )
        (
            self.app.system()
            .get_reservation()
            .reservation_id("res1")
            .execute()
            .should_succeed()
            .has_valid_id()
            .has_status("active")
            .has_car_id("car1")
            .has_charging_point_id(CHARGING_POINT_ID)
        )

    # ------------------------------------------------------------------
    # Reservations – negative
    # ------------------------------------------------------------------

    @channel(ChannelType.API)
    def test_should_not_create_reservation_with_not_existent_car(self) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        (
            self.app.system()
            .create_reservation()
            .car_id(str(uuid4()))
            .charging_point_id(str(uuid4()))
            .execute()
            .should_fail()
            .error_message("Car not found")
        )

    @channel(ChannelType.API)
    def test_should_not_create_reservation_with_not_existent_charging_point(
        self,
    ) -> None:
        self.app.system().login().username("addisonw").password(
            "addisonwpass"
        ).execute().should_succeed()
        self.app.system().add_car().car_id("car1").execute().should_succeed()
        (
            self.app.system()
            .create_reservation()
            .car_id("car1")
            .charging_point_id(str(uuid4()))
            .execute()
            .should_fail()
            .error_message(
                "Charging point is not available during the requested time. Charging point not found"
            )
        )
