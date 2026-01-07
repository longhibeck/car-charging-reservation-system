from system_test.core.clients.system.api.car_charging_reservation_api_client import CarChargingReservationApiClient


def test_should_login(car_charging_reservation_api_client: CarChargingReservationApiClient):
    """Test successful login with valid credentials"""
    # Login
    response = car_charging_reservation_api_client.auth().login(
        username="addisonw", 
        password="addisonwpass"
    )
    
    # Assert login successful
    auth_data = car_charging_reservation_api_client.auth().assert_login_successful(response)
    
    # Verify response structure
    assert auth_data["access_token"] is not None
    assert auth_data["refresh_token"] is not None
    assert auth_data["token_type"] == "bearer"
    assert auth_data["user"]["id"] is not None
    assert auth_data["user"]["username"] == "addisonw"
    assert auth_data["user"]["external_user_id"] is not None


def test_should_should_display_current_user(logged_in_api_context):
    """Test getting current authenticated user details"""
    # This test still uses the old fixture since it needs authentication
    # In a real scenario, you'd want to add auth handling to the API client
    response = logged_in_api_context.get("/api/v1/auth/me")
    response_json = response.json()
    assert response.ok
    assert response_json["id"] is not None
    assert response_json["username"] == "addisonw"
    assert response_json["external_user_id"] > 0
