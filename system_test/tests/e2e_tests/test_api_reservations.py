from datetime import datetime, timedelta, timezone

from system_test.core.clients.system.api.car_charging_reservation_api_client import CarChargingReservationApiClient


def to_zulu_format(dt: datetime) -> str:
    """Convert datetime to Zulu format (Z suffix)"""
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def parse_zulu_time(zulu_str: str) -> datetime:
    """Parse Zulu format string to datetime"""
    return datetime.strptime(zulu_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=timezone.utc
    )


def test_should_list_reservations(authenticated_api_client: CarChargingReservationApiClient):
    """Test that reservations endpoint returns empty list initially"""
    response = authenticated_api_client.reservations().list_reservations()
    reservations = authenticated_api_client.reservations().assert_reservations_listed_successfully(response)
    
    assert isinstance(reservations, list), "Should return a flat array"


def test_should_create_reservation(authenticated_api_client: CarChargingReservationApiClient):
    """Test creating a new reservation"""
    # Record when we start the test
    test_start = datetime.now(timezone.utc)

    # First create a car
    car_response = authenticated_api_client.cars().create_car(
        name="Tesla Model 3",
        connector_types=["Type 2", "CCS"],
        battery_charge_limit=100,
        battery_size=75,
        max_kw_ac=11,
        max_kw_dc=250
    )
    car = authenticated_api_client.cars().assert_car_created_successfully(car_response)
    car_id = car["id"]

    # Create a reservation
    start_time = datetime.now(timezone.utc) + timedelta(hours=1)
    end_time = start_time + timedelta(hours=2)

    response = authenticated_api_client.reservations().create_reservation(
        car_id=car_id,
        charging_point_id="550e8400-e29b-41d4-a716-446655440001",  # From data.json
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat()
    )

    reservation = authenticated_api_client.reservations().assert_reservation_created_successfully(response)
    test_end = datetime.now(timezone.utc)

    assert reservation["car_id"] == car_id
    assert reservation["charging_point_id"] == "550e8400-e29b-41d4-a716-446655440001"
    assert reservation["status"] == "active"
    assert reservation["start_time"] == to_zulu_format(start_time)
    assert reservation["end_time"] == to_zulu_format(end_time)

    # Assert created_at and updated_at
    assert "created_at" in reservation, "created_at field should exist"
    assert "updated_at" in reservation, "updated_at field should exist"
    
    # Parse the timestamps
    created_at = parse_zulu_time(reservation["created_at"])
    updated_at = parse_zulu_time(reservation["updated_at"])
    
    # Assert timestamps are recent (within test execution time)
    assert test_start <= created_at <= test_end
    assert test_start <= updated_at <= test_end

def test_should_get_reservation(authenticated_api_client: CarChargingReservationApiClient):
    """Test getting a specific reservation"""
    # Record when we start the test
    test_start = datetime.now(timezone.utc)

    # Get current authenticated user
    user_response = authenticated_api_client.auth().get_current_user()
    user = authenticated_api_client.auth().assert_current_user_retrieved_successfully(user_response)
    user_id = user["id"]

    # Create a car first
    car_response = authenticated_api_client.cars().create_car(
        name="BMW iX3",
        connector_types=["Type 2", "CCS"],
        battery_charge_limit=100,
        battery_size=80,
        max_kw_ac=11,
        max_kw_dc=150
    )
    car = authenticated_api_client.cars().assert_car_created_successfully(car_response)
    car_id = car["id"]

    # Create a reservation
    start_time = datetime.now(timezone.utc) + timedelta(hours=2)
    end_time = start_time + timedelta(hours=1)

    create_response = authenticated_api_client.reservations().create_reservation(
        car_id=car_id,
        charging_point_id="550e8400-e29b-41d4-a716-446655440003",
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat()
    )
    created_reservation = authenticated_api_client.reservations().assert_reservation_created_successfully(create_response)
    reservation_id = created_reservation["id"]

    test_end = datetime.now(timezone.utc)

    # Get the reservation
    get_response = authenticated_api_client.reservations().get_reservation(reservation_id)
    reservation = authenticated_api_client.reservations().assert_reservation_retrieved_successfully(get_response)

    assert reservation["id"] == reservation_id
    assert reservation["car_id"] == car_id
    assert reservation["user_id"] == user_id
    assert reservation["status"] == "active"
    assert reservation["start_time"] == to_zulu_format(start_time)
    assert reservation["end_time"] == to_zulu_format(end_time)
    assert reservation["created_at"]
    assert reservation["updated_at"]

    # Assert created_at and updated_at exist and are valid
    assert "created_at" in reservation, "created_at field should exist"
    assert "updated_at" in reservation, "updated_at field should exist"
    
    # Parse the timestamps
    created_at = parse_zulu_time(reservation["created_at"])
    updated_at = parse_zulu_time(reservation["updated_at"])
    
    # Assert timestamps are recent (created during test execution)
    assert test_start <= created_at <= test_end
    assert test_start <= updated_at <= test_end
