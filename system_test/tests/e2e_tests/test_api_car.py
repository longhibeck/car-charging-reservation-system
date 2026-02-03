from system_test.core.matchers.result_matchers import to_be_success, to_be_failure_with
import pytest


def test_should_list_cars(authenticated_api_driver) -> None:
    result = authenticated_api_driver.list_cars()
    to_be_success(result)


def test_should_add_car(authenticated_api_driver) -> None:
    add_car_result = authenticated_api_driver.add_car(
        name="BYD Seal U",
        connector_types=["CCS"],
        battery_charge_limit=100,
        battery_size=87,
        max_kw_ac=11,
        max_kw_dc=15,
    )
    to_be_success(add_car_result)


@pytest.mark.parametrize(
    "connector_types",
    [
        (["Type 2", "Schuko"]),
        (["Type 2", "CCS"]),
        (["Type 2", "CCS", "Schuko"]),
    ],
)
def test_should_add_car_with_multiple_valid_connector_types(
    authenticated_api_driver, connector_types
):
    add_car_result = authenticated_api_driver.add_car(
        name="BYD Seal U",
        connector_types=connector_types,
        battery_charge_limit=100,
        battery_size=87,
        max_kw_ac=11,
        max_kw_dc=15,
    )
    to_be_success(add_car_result)

@pytest.mark.parametrize("value", (0, -10, -20))
def test_should_not_create_car_with_zero_or_negative_battery_charge_limit(
    authenticated_api_driver, value
):
    add_car_result = authenticated_api_driver.add_car(
        name="Invalid Car",
        connector_types=["CCS"],
        battery_charge_limit=value,
        battery_size=87,
        max_kw_ac=11,
        max_kw_dc=15,
    )
    to_be_failure_with(add_car_result, "Input should be greater than 0")

@pytest.mark.parametrize("value", (101, 200, 150))
def test_should_not_create_car_with_over_hundred_battery_charge_limit(
    authenticated_api_driver, value
):
    add_car_result = authenticated_api_driver.add_car(
        name="Invalid Car",
        connector_types=["CCS"],
        battery_charge_limit=value,
        battery_size=87,
        max_kw_ac=11,
        max_kw_dc=15,
    )
    to_be_failure_with(add_car_result, "Input should be less than or equal to 100")


def test_should_not_add_car_with_invalid_data_type(authenticated_api_driver):
    add_car_result = authenticated_api_driver.add_car(
        name="Invalid Car",
        connector_types=["CCS"],
        battery_charge_limit=100,
        battery_size="not-a-number",
        max_kw_ac=11,
        max_kw_dc=15,
    )
    to_be_failure_with(add_car_result, "Input should be a valid integer, unable to parse string as an integer")


def test_should_update_car_successfully(
    authenticated_api_driver,
):
    add_car_result = authenticated_api_driver.add_car(
        name="Tesla Model 3",
        connector_types=["CCS"],
        battery_charge_limit=90,
        battery_size=75,
        max_kw_ac=11,
        max_kw_dc=250,
    )
    to_be_success(add_car_result)
    car = add_car_result.get_value()
    car_id = car["id"]

    update_result = authenticated_api_driver.update_car(
        car_id=car_id,
        name="Tesla Model 3 Updated",
        connector_types=["CCS", "Type 2"],
        battery_charge_limit=95,
        battery_size=80,
        max_kw_ac=22,
        max_kw_dc=300,
    )
    to_be_success(update_result)

def test_should_delete_car_successfully(
    authenticated_api_driver,
):
    add_car_result = authenticated_api_driver.add_car(
        name="Nissan Leaf",
        connector_types=["CHAdeMO"],
        battery_charge_limit=80,
        battery_size=40,
        max_kw_ac=6,
        max_kw_dc=50,
    )
    to_be_success(add_car_result)
    car = add_car_result.get_value()
    car_id = car["id"]

    delete_result = authenticated_api_driver.delete_car(car_id=car_id)
    to_be_success(delete_result)