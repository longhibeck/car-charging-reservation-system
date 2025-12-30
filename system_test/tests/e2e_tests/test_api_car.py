import pytest

from system_test.core.clients.system.api.car_charging_reservation_api_client import (
    CarChargingReservationApiClient,
)


def test_should_list_cars(authenticated_api_client: CarChargingReservationApiClient):
    """Test listing cars returns empty list initially"""
    response = authenticated_api_client.cars().list_cars()
    cars = authenticated_api_client.cars().assert_cars_listed_successfully(response)
    assert cars == []


def test_should_create_car(authenticated_api_client: CarChargingReservationApiClient):
    """Test creating a new car (alternative: individual parameters)"""
    name = "BYD Seal U"
    connector_types = ["CCS"]
    battery_charge_limit = 100
    battery_size = 87
    max_kw_ac = 11
    max_kw_dc = 15

    response = authenticated_api_client.cars().create_car(
        name=name,
        connector_types=connector_types,
        battery_charge_limit=battery_charge_limit,
        battery_size=battery_size,
        max_kw_ac=max_kw_ac,
        max_kw_dc=max_kw_dc,
    )

    car = authenticated_api_client.cars().assert_car_created_successfully(response)
    assert car["id"] is not None
    assert car["name"] == name
    assert car["connector_types"] == connector_types
    assert car["battery_charge_limit"] == battery_charge_limit
    assert car["battery_size"] == battery_size
    assert car["max_kw_ac"] == max_kw_ac
    assert car["max_kw_dc"] == max_kw_dc

@pytest.mark.parametrize(
    "connector_types",
    [
        (["Type 2", "Schuko"]),
        (["Type 2", "CCS"]),
        (["Type 2", "CCS", "Schuko"]),

    ],)
def test_should_create_car_with_multiple_valid_connector_types(
    authenticated_api_client: CarChargingReservationApiClient, connector_types
):
    """Test creating a new car (alternative: individual parameters)"""
    name = "BYD Seal U"
    battery_charge_limit = 100
    battery_size = 87
    max_kw_ac = 11
    max_kw_dc = 15

    response = authenticated_api_client.cars().create_car(
        name=name,
        connector_types=connector_types,
        battery_charge_limit=battery_charge_limit,
        battery_size=battery_size,
        max_kw_ac=max_kw_ac,
        max_kw_dc=max_kw_dc,
    )

    car = authenticated_api_client.cars().assert_car_created_successfully(response)
    assert car["id"] is not None
    assert car["name"] == name
    assert car["connector_types"] == sorted(connector_types)
    assert car["battery_charge_limit"] == battery_charge_limit
    assert car["battery_size"] == battery_size
    assert car["max_kw_ac"] == max_kw_ac
    assert car["max_kw_dc"] == max_kw_dc


@pytest.mark.parametrize("value", (0, 120, -10))
def test_should_not_create_car_with_invalid_battery_charge_limit(
    authenticated_api_client: CarChargingReservationApiClient, value
):
    """Test car creation fails with invalid battery charge limit"""

    name = "BYD Seal U"
    connector_types = ["CCS"]
    battery_charge_limit = value
    battery_size = 87
    max_kw_ac = 11
    max_kw_dc = 150

    response = authenticated_api_client.cars().create_car(
        name=name,
        connector_types=connector_types,
        battery_charge_limit=battery_charge_limit,
        battery_size=battery_size,
        max_kw_ac=max_kw_ac,
        max_kw_dc=max_kw_dc,
    )

    authenticated_api_client.cars().assert_car_creation_failed(response)
    error_message = authenticated_api_client.cars().get_error_message(response)
    assert "battery_charge_limit" in error_message.lower()


def test_should_not_create_car_with_invalid_data_type(
    authenticated_api_client: CarChargingReservationApiClient,
):
    """Test car creation fails with invalid data type"""

    name = "BYD Seal U"
    connector_types = ["CCS"]
    battery_charge_limit = 100
    battery_size = "not a number"
    max_kw_ac = 11
    max_kw_dc = 150

    response = authenticated_api_client.cars().create_car(
        name=name,
        connector_types=connector_types,
        battery_charge_limit=battery_charge_limit,
        battery_size=battery_size,
        max_kw_ac=max_kw_ac,
        max_kw_dc=max_kw_dc,
    )

    authenticated_api_client.cars().assert_car_creation_failed(response)
    error_message = authenticated_api_client.cars().get_error_message(response)
    assert "battery_size" in error_message.lower()


def test_should_update_car(authenticated_api_client: CarChargingReservationApiClient):
    """Test updating an existing car"""
    # Create car
    create_response = authenticated_api_client.cars().create_car(
        name="BYD Seal U",
        connector_types=["CCS"],
        battery_charge_limit=100,
        battery_size=87,
        max_kw_ac=11,
        max_kw_dc=150,
    )
    created_car = authenticated_api_client.cars().assert_car_created_successfully(
        create_response
    )
    car_id = created_car["id"]

    # Update car
    update_response = authenticated_api_client.cars().update_car(
        car_id=car_id,
        name="BYD Seal",
        connector_types=["Type 2"],
        battery_charge_limit=80,
        battery_size=87,
        max_kw_ac=11,
        max_kw_dc=150,
    )

    updated_car = authenticated_api_client.cars().assert_car_updated_successfully(
        update_response
    )
    assert updated_car["id"] == car_id
    assert updated_car["name"] == "BYD Seal"
    assert updated_car["connector_types"] == ["Type 2"]
    assert updated_car["battery_charge_limit"] == 80


def test_should_get_car(authenticated_api_client: CarChargingReservationApiClient):
    """Test getting a specific car by ID"""

    name = "BYD Seal U"
    connector_types = ["CCS"]
    battery_charge_limit = 100
    battery_size = 87
    max_kw_ac = 11
    max_kw_dc = 150

    # Create car
    create_response = authenticated_api_client.cars().create_car(
        name=name,
        connector_types=connector_types,
        battery_charge_limit=battery_charge_limit,
        battery_size=battery_size,
        max_kw_ac=max_kw_ac,
        max_kw_dc=max_kw_dc,
    )
    created_car = authenticated_api_client.cars().assert_car_created_successfully(
        create_response
    )
    car_id = created_car["id"]

    # Get car
    get_response = authenticated_api_client.cars().get_car(car_id)
    car = authenticated_api_client.cars().assert_car_retrieved_successfully(
        get_response
    )

    assert car["id"] == car_id
    assert car["name"] == name
    assert car["connector_types"] == connector_types
    assert car["battery_charge_limit"] == battery_charge_limit
    assert car["battery_size"] == battery_size
    assert car["max_kw_ac"] == max_kw_ac
    assert car["max_kw_dc"] == max_kw_dc
