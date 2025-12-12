from datetime import datetime, timedelta, timezone


def test_should_list_reservations(logged_in_api_context):
    """Test that reservations endpoint returns empty list initially"""
    response = logged_in_api_context.get("/api/v1/reservations/")

    assert response.status == 200
    assert "application/json" in response.headers.get("content-type", "")

    data = response.json()
    assert isinstance(data, list), "Should return a flat array"


def test_should_create_reservation(logged_in_api_context):
    """Test creating a new reservation"""

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
    assert reservation["car_id"] == car_id
    assert reservation["charging_point_id"] == "550e8400-e29b-41d4-a716-446655440001"


def test_should_get_reservation(logged_in_api_context):
    """Test getting a specific reservation"""

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

    # Get the reservation
    get_response = logged_in_api_context.get(f"/api/v1/reservations/{reservation_id}")
    assert get_response.status == 200

    reservation = get_response.json()
    assert reservation["id"] == reservation_id
    assert reservation["car_id"] == car_id
    assert reservation["user_id"] == user_id
