"""
E2E tests for the car charging reservation system.

Mirrors PlaceOrderPositiveTest / PlaceOrderNegativeTest from mod06 in the
optivem/shop reference implementation: a single test class decorated with
@channel(API, UI) so that every test method runs once per channel.

The correct driver (API or UI) is resolved automatically from ChannelContext
inside DriverFactory.create_system_driver_for_current_channel().
"""

import pytest
from functools import wraps
from system_test.channel import channel, ChannelType
from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.drivers.commons.utils.datetime_utils import DateTimeUtils
from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.system.commons.dtos.auth_request import LoginRequest
from system_test.core.drivers.system.commons.dtos.car_request import AddCarRequest, UpdateCarRequest
from system_test.core.drivers.system.commons.dtos.reservation_request import CreateReservationRequest
from uuid import uuid4


def login_as(username: str = "addisonw", password: str = "addisonwpass"):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = self.system_driver.login(LoginRequest(username=username, password=password))
            ResultAssert.assert_that_result(result).is_success()
            return func(self, *args, **kwargs)
        return wrapper
    return decorator


class TestE2e:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.system_driver = DriverFactory.create_system_driver_for_current_channel()
        self.charging_points_api_driver = DriverFactory.create_charging_points_api_driver()
        self.auth_api_driver = DriverFactory.create_auth_api_driver()
        yield
        self.system_driver.close()
        self.charging_points_api_driver.close()
        self.auth_api_driver.close()

    # ------------------------------------------------------------------
    # Auth
    # ------------------------------------------------------------------

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_login(self) -> None:
        result = self.system_driver.login(LoginRequest(username="addisonw", password="addisonwpass"))
        ResultAssert.assert_that_result(result).is_success()

    @channel(ChannelType.API, ChannelType.UI)
    def test_should_not_login_with_invalid_credentials(self) -> None:
        result = self.system_driver.login(LoginRequest(username="invalid_user", password="invalid_pass"))
        ResultAssert.assert_that_result(result).is_failure("Invalid credentials")

    @channel(ChannelType.API)
    @login_as()
    def test_should_get_current_user(self) -> None:
        current_user_result = self.system_driver.get_current_user()
        ResultAssert.assert_that_result(current_user_result).is_success()

    # ------------------------------------------------------------------
    # Cars – positive
    # ------------------------------------------------------------------

    @channel(ChannelType.API, ChannelType.UI)
    @login_as()
    def test_should_add_car(self) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="BYD Seal U",
                connector_types=["CCS"],
                battery_charge_limit=100,
                battery_size=87,
                max_kw_ac=11,
                max_kw_dc=15,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_success()

    @channel(ChannelType.API, ChannelType.UI)
    @login_as()
    def test_should_list_cars(self) -> None:
        list_cars_result = self.system_driver.list_cars()
        ResultAssert.assert_that_result(list_cars_result).is_success()

    @channel(ChannelType.API, ChannelType.UI)
    @pytest.mark.parametrize(
        "connector_types",
        [
            ["Type 2", "Schuko"],
            ["Type 2", "CCS"],
            ["Type 2", "CCS", "Schuko"],
        ],
    )
    @login_as()
    def test_should_add_car_with_multiple_valid_connector_types(self, connector_types) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="BYD Seal U",
                connector_types=connector_types,
                battery_charge_limit=100,
                battery_size=87,
                max_kw_ac=11,
                max_kw_dc=15,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_success()

    @channel(ChannelType.API)
    @login_as()
    def test_should_update_car_successfully(self) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Tesla Model 3",
                connector_types=["CCS"],
                battery_charge_limit=90,
                battery_size=75,
                max_kw_ac=11,
                max_kw_dc=250,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_success()
        car_id = add_car_result.get_value()["id"]

        update_result = self.system_driver.update_car(
            car_id,
            UpdateCarRequest(
                name="Tesla Model 3 Updated",
                connector_types=["CCS", "Type 2"],
                battery_charge_limit=95,
                battery_size=80,
                max_kw_ac=22,
                max_kw_dc=300,
            ),
        )
        ResultAssert.assert_that_result(update_result).is_success()

    @channel(ChannelType.API)
    @login_as()
    def test_should_delete_car_successfully(self) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Nissan Leaf",
                connector_types=["CHAdeMO"],
                battery_charge_limit=80,
                battery_size=40,
                max_kw_ac=6,
                max_kw_dc=50,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_success()
        car_id = add_car_result.get_value()["id"]

        delete_result = self.system_driver.delete_car(car_id=car_id)
        ResultAssert.assert_that_result(delete_result).is_success()

    # ------------------------------------------------------------------
    # Cars – negative
    # ------------------------------------------------------------------

    @channel(ChannelType.API)
    @login_as()
    def test_should_not_add_car_with_invalid_data_type(self) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Invalid Car",
                connector_types=["CCS"],
                battery_charge_limit=100,
                battery_size="not-a-number",
                max_kw_ac=11,
                max_kw_dc=15,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_failure(
            "Input should be a valid integer, unable to parse string as an integer"
        )

    @channel(ChannelType.API)
    @pytest.mark.parametrize("value", [0, -10, -20])
    @login_as()
    def test_should_not_create_car_with_zero_or_negative_battery_charge_limit(self, value) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Invalid Car",
                connector_types=["CCS"],
                battery_charge_limit=value,
                battery_size=87,
                max_kw_ac=11,
                max_kw_dc=15,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_failure(
            "Input should be greater than 0"
        )

    @channel(ChannelType.API)
    @pytest.mark.parametrize("value", [101, 200, 150])
    @login_as()
    def test_should_not_create_car_with_over_hundred_battery_charge_limit(self, value) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Invalid Car",
                connector_types=["CCS"],
                battery_charge_limit=value,
                battery_size=87,
                max_kw_ac=11,
                max_kw_dc=15,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_failure(
            "Input should be less than or equal to 100"
        )

    # ------------------------------------------------------------------
    # Reservations – positive
    # ------------------------------------------------------------------

    @channel(ChannelType.API)
    @login_as()
    def test_should_list_reservations(self) -> None:
        list_reservations_result = self.system_driver.list_reservations()
        ResultAssert.assert_that_result(list_reservations_result).is_success()

    @channel(ChannelType.API)
    @login_as()
    def test_should_create_reservation_successfully(self) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Test Car",
                connector_types=["CCS"],
                battery_charge_limit=80,
                battery_size=500,
                max_kw_ac=22,
                max_kw_dc=150,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_success()
        car_id = add_car_result.get_value()["id"]

        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            CreateReservationRequest(
                car_id=car_id,
                charging_point_id="550e8400-e29b-41d4-a716-446655440001",
                start_time=start_time,
                end_time=end_time,
            )
        )
        ResultAssert.assert_that_result(add_reservation_result).is_success()

    @channel(ChannelType.API)
    @login_as()
    def test_should_get_reservation_successfully(self) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Test Car",
                connector_types=["CCS"],
                battery_charge_limit=80,
                battery_size=500,
                max_kw_ac=22,
                max_kw_dc=150,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_success()
        car_id = add_car_result.get_value()["id"]

        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            CreateReservationRequest(
                car_id=car_id,
                charging_point_id="550e8400-e29b-41d4-a716-446655440001",
                start_time=start_time,
                end_time=end_time,
            )
        )
        ResultAssert.assert_that_result(add_reservation_result).is_success()
        reservation_id = add_reservation_result.get_value()["id"]

        get_reservation_result = self.system_driver.get_reservation(reservation_id)
        ResultAssert.assert_that_result(get_reservation_result).is_success()

    # ------------------------------------------------------------------
    # Reservations – negative
    # ------------------------------------------------------------------

    @channel(ChannelType.API)
    @login_as()
    def test_should_not_create_reservation_with_not_existent_car(self) -> None:
        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            CreateReservationRequest(
                car_id=str(uuid4()),
                charging_point_id=str(uuid4()),
                start_time=start_time,
                end_time=end_time,
            )
        )
        ResultAssert.assert_that_result(add_reservation_result).is_failure("Car not found")

    @channel(ChannelType.API)
    @login_as()
    def test_should_not_create_reservation_with_not_existent_charging_point(self) -> None:
        add_car_result = self.system_driver.add_car(
            AddCarRequest(
                name="Test Car",
                connector_types=["CCS"],
                battery_charge_limit=80,
                battery_size=500,
                max_kw_ac=22,
                max_kw_dc=150,
            )
        )
        ResultAssert.assert_that_result(add_car_result).is_success()
        car_id = add_car_result.get_value()["id"]

        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            CreateReservationRequest(
                car_id=car_id,
                charging_point_id=str(uuid4()),
                start_time=start_time,
                end_time=end_time,
            )
        )
        ResultAssert.assert_that_result(add_reservation_result).is_failure(
            "Charging point is not available during the requested time. Charging point not found"
        )
