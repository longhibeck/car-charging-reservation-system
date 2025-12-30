from system_test.core.clients.system.ui.car_charging_reservation_ui_client import CarChargingReservationUiClient


def test_should_login_successfully(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test successful login with method chaining"""
    # Navigate to home - redirects to login
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    
    # Login and get home page back
    home_page = login_page.login(username="addisonw", password="addisonwpass")
    
    # Assert we're on home page
    home_page.assert_loaded()


def test_should_not_login_with_invalid_credentials(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test login fails with invalid credentials"""
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    
    # Try to login - will fail, so don't assign return value
    login_page.fill_username("invalid_user")
    login_page.fill_password("invalid_pass")
    login_page.click_login()
    
    # Still on login page with error
    login_page.assert_login_failed()


def test_should_not_login_with_missing_password(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test HTML5 validation prevents login"""
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    
    login_page.fill_username("user")
    login_page.click_login()
    
    login_page.assert_password_validation_message("Please fill out this field.")