from system_test.tests.e2e_tests.test_base_e2e import BaseE2eTest, login_as
from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.drivers.commons.utils.datetime_utils import DateTimeUtils
from uuid import uuid4


class TestApiE2e(BaseE2eTest):
    def create_system_driver(self):
        return DriverFactory.create_system_api_driver()

    @login_as()
    def test_should_get_current_user(self) -> None:
        current_user_result = self.system_driver.get_current_user()
        ResultAssert.assert_that_result(current_user_result).is_success()

    @login_as()
    def test_should_not_add_car_with_invalid_data_type(self) -> None:
        add_car_result = self.system_driver.add_car(
            name="Invalid Car",
            connector_types=["CCS"],
            battery_charge_limit=100,
            battery_size="not-a-number",
            max_kw_ac=11,
            max_kw_dc=15,
        )
        ResultAssert.assert_that_result(add_car_result).is_failure(
            "Input should be a valid integer, unable to parse string as an integer"
        )

    @login_as()
    def test_should_update_car_successfully(
        self,
    ) -> None:
        add_car_result = self.system_driver.add_car(
            name="Tesla Model 3",
            connector_types=["CCS"],
            battery_charge_limit=90,
            battery_size=75,
            max_kw_ac=11,
            max_kw_dc=250,
        )
        ResultAssert.assert_that_result(add_car_result).is_success()
        car = add_car_result.get_value()
        car_id = car["id"]

        update_result = self.system_driver.update_car(
            car_id=car_id,
            name="Tesla Model 3 Updated",
            connector_types=["CCS", "Type 2"],
            battery_charge_limit=95,
            battery_size=80,
            max_kw_ac=22,
            max_kw_dc=300,
        )
        ResultAssert.assert_that_result(update_result).is_success()

    @login_as()
    def test_should_delete_car_successfully(
        self,
    ) -> None:
        add_car_result = self.system_driver.add_car(
            name="Nissan Leaf",
            connector_types=["CHAdeMO"],
            battery_charge_limit=80,
            battery_size=40,
            max_kw_ac=6,
            max_kw_dc=50,
        )
        ResultAssert.assert_that_result(add_car_result).is_success()
        car = add_car_result.get_value()
        car_id = car["id"]

        delete_result = self.system_driver.delete_car(car_id=car_id)
        ResultAssert.assert_that_result(delete_result).is_success()

    @login_as()
    def test_should_list_reservations(self) -> None:
        list_reservations_result = self.system_driver.list_reservations()
        ResultAssert.assert_that_result(list_reservations_result).is_success()
        list_reservations_result = self.system_driver.list_reservations()
        ResultAssert.assert_that_result(list_reservations_result).is_success()

    @login_as()
    def test_should_not_create_reservation_with_not_existent_car(
        self,
    ) -> None:
        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            car_id=str(uuid4()),
            charging_point_id=str(uuid4()),
            start_time=start_time,
            end_time=end_time,
        )
        ResultAssert.assert_that_result(add_reservation_result).is_failure(
            "Car not found"
        )

    @login_as()
    def test_should_not_create_reservation_with_not_existent_charging_point(
        self,
    ) -> None:

        add_car_result = self.system_driver.add_car(
            name="Test Car",
            connector_types=["CCS"],
            battery_charge_limit=80,
            battery_size=500,
            max_kw_ac=22,
            max_kw_dc=150,
        )
        ResultAssert.assert_that_result(add_car_result).is_success()

        car = add_car_result.get_value()
        car_id = car["id"]
        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            car_id=car_id,
            charging_point_id=str(uuid4()),
            start_time=start_time,
            end_time=end_time,
        )
        ResultAssert.assert_that_result(add_reservation_result).is_failure(
            "Charging point is not available during the requested time. Charging point not found"
        )

    @login_as()
    def test_should_create_reservation_successfully(
        self,
    ) -> None:
        add_car_result = self.system_driver.add_car(
            name="Test Car",
            connector_types=["CCS"],
            battery_charge_limit=80,
            battery_size=500,
            max_kw_ac=22,
            max_kw_dc=150,
        )
        ResultAssert.assert_that_result(add_car_result).is_success()

        car = add_car_result.get_value()
        car_id = car["id"]
        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            car_id=car_id,
            charging_point_id="550e8400-e29b-41d4-a716-446655440001",
            start_time=start_time,
            end_time=end_time,
        )
        ResultAssert.assert_that_result(add_reservation_result).is_success()

    @login_as()
    def test_should_get_reservation_successfully(
        self,
    ) -> None:
        add_car_result = self.system_driver.add_car(
            name="Test Car",
            connector_types=["CCS"],
            battery_charge_limit=80,
            battery_size=500,
            max_kw_ac=22,
            max_kw_dc=150,
        )
        ResultAssert.assert_that_result(add_car_result).is_success()

        car = add_car_result.get_value()
        car_id = car["id"]
        now = DateTimeUtils.get_current_zulu_time()
        start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
        end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

        add_reservation_result = self.system_driver.create_reservation(
            car_id=car_id,
            charging_point_id="550e8400-e29b-41d4-a716-446655440001",
            start_time=start_time,
            end_time=end_time,
        )
        ResultAssert.assert_that_result(add_reservation_result).is_success()

        reservation = add_reservation_result.get_value()
        reservation_id = reservation["id"]

        get_reservation_result = self.system_driver.get_reservation(reservation_id)
        ResultAssert.assert_that_result(get_reservation_result).is_success()
