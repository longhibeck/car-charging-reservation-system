from system_test.core.drivers.commons.utils.datetime_utils import DateTimeUtils
from system_test.core.matchers.result_matchers import to_be_success, to_be_failure_with
import uuid


def test_should_list_reservations(authenticated_api_driver) -> None:
    result = authenticated_api_driver.list_reservations()
    to_be_success(result)


def test_should_not_create_reservation_with_not_existent_car(
    authenticated_api_driver,
) -> None:
    now = DateTimeUtils.get_current_zulu_time()
    start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
    end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

    add_reservation_result = authenticated_api_driver.create_reservation(
        car_id=str(uuid.uuid4()),
        charging_point_id=str(uuid.uuid4()),
        start_time=start_time,
        end_time=end_time,
    )
    to_be_failure_with(add_reservation_result, "Car not found")


def test_should_not_create_reservation_with_not_existent_charging_point(
    authenticated_api_driver,
) -> None:
    add_car_result = authenticated_api_driver.add_car(
        name="Test Car",
        connector_types=["CCS"],
        battery_charge_limit=80,
        battery_size=500,
        max_kw_ac=22,
        max_kw_dc=150,
    )
    to_be_success(add_car_result)

    car = add_car_result.get_value()
    car_id = car["id"]
    now = DateTimeUtils.get_current_zulu_time()
    start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
    end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

    add_reservation_result = authenticated_api_driver.create_reservation(
        car_id=car_id,
        charging_point_id=str(uuid.uuid4()),
        start_time=start_time,
        end_time=end_time,
    )
    to_be_failure_with(add_reservation_result, "Charging point not found")


def test_should_create_reservation_successfully(
    authenticated_api_driver,
) -> None:
    add_car_result = authenticated_api_driver.add_car(
        name="Test Car",
        connector_types=["CCS"],
        battery_charge_limit=80,
        battery_size=500,
        max_kw_ac=22,
        max_kw_dc=150,
    )
    to_be_success(add_car_result)

    car = add_car_result.get_value()
    car_id = car["id"]
    now = DateTimeUtils.get_current_zulu_time()
    start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
    end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

    add_reservation_result = authenticated_api_driver.create_reservation(
        car_id=car_id,
        charging_point_id="550e8400-e29b-41d4-a716-446655440001",
        start_time=start_time,
        end_time=end_time,
    )
    to_be_success(add_reservation_result)


def test_should_get_reservation_successfully(
    authenticated_api_driver,
) -> None:
    add_car_result = authenticated_api_driver.add_car(
        name="Test Car",
        connector_types=["CCS"],
        battery_charge_limit=80,
        battery_size=500,
        max_kw_ac=22,
        max_kw_dc=150,
    )
    to_be_success(add_car_result)

    car = add_car_result.get_value()
    car_id = car["id"]
    now = DateTimeUtils.get_current_zulu_time()
    start_time = DateTimeUtils.add_hours_to_zulu_time(now, 1)
    end_time = DateTimeUtils.add_hours_to_zulu_time(start_time, 4)

    add_reservation_result = authenticated_api_driver.create_reservation(
        car_id=car_id,
        charging_point_id="550e8400-e29b-41d4-a716-446655440001",
        start_time=start_time,
        end_time=end_time,
    )
    to_be_success(add_reservation_result)

    reservation = add_reservation_result.get_value()
    reservation_id = reservation["id"]

    get_reservation_result = authenticated_api_driver.get_reservation(reservation_id)
    to_be_success(get_reservation_result)
