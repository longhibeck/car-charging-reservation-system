from datetime import datetime, timedelta, timezone


def to_zulu_format(dt: datetime) -> str:
    """Convert datetime to Zulu format (Z suffix)"""
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def parse_zulu_time(zulu_str: str) -> datetime:
    """Parse Zulu format string to datetime"""
    return datetime.strptime(zulu_str, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=timezone.utc
    )


def test_should_list_reservations(logged_in_api_context):
    """Test that reservations endpoint returns empty list initially"""
    response = logged_in_api_context.get("/api/v1/reservations/")

    assert response.status == 200
    assert "application/json" in response.headers.get("content-type", "")

    data = response.json()
    assert isinstance(data, list), "Should return a flat array"


def test_should_create_reservation(logged_in_api_context):
    """Test creating a new reservation"""

    # Record when we start the test
    test_start = datetime.now(timezone.utc)

    # First create a car
    car_data = {
        "name": "Tesla Model 3",
        "connector_types": ["Type 2", "CCS"],
        "battery_charge_limit": 100,
        "battery_size": 75,
        "max_kw_ac": 11,
        "max_kw_dc": 250,
    }
    car_response = logged_in_api_context.post("/api/v1/cars/", data=car_data)
    assert car_response.status == 201
    car_id = car_response.json()["id"]

    # Create a reservation
    start_time = datetime.now(timezone.utc) + timedelta(hours=1)
    end_time = start_time + timedelta(hours=2)

    reservation_data = {
        "car_id": car_id,
        "charging_point_id": "550e8400-e29b-41d4-a716-446655440001",  # From data.json
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
    }

    response = logged_in_api_context.post(
        "/api/v1/reservations/", data=reservation_data
    )

    assert response.status == 201, f"Failed to create reservation: {response.text()}"

    reservation = response.json()
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

def test_should_get_reservation(logged_in_api_context):
    """Test getting a specific reservation"""

    # Record when we start the test
    test_start = datetime.now(timezone.utc)

    # Get current authenticated user
    user_response = logged_in_api_context.get("/api/v1/auth/me")
    assert user_response.status == 200
    user_id = user_response.json()["id"]

    # Create a reservation first
    car_data = {
        "name": "BMW iX3",
        "connector_types": ["Type 2", "CCS"],
        "battery_charge_limit": 100,
        "battery_size": 80,
        "max_kw_ac": 11,
        "max_kw_dc": 150,
    }
    car_response = logged_in_api_context.post("/api/v1/cars/", data=car_data)
    assert car_response.status == 201
    car_id = car_response.json()["id"]

    start_time = datetime.now(timezone.utc) + timedelta(hours=2)
    end_time = start_time + timedelta(hours=1)

    reservation_data = {
        "car_id": car_id,
        "charging_point_id": "550e8400-e29b-41d4-a716-446655440003",
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
    }

    create_response = logged_in_api_context.post(
        "/api/v1/reservations/", data=reservation_data
    )
    assert create_response.status == 201
    reservation_id = create_response.json()["id"]

    test_end = datetime.now(timezone.utc)

    # Get the reservation
    get_response = logged_in_api_context.get(f"/api/v1/reservations/{reservation_id}")
    assert get_response.status == 200

    reservation = get_response.json()

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
