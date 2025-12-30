from system_test.core.clients.system.ui.car_charging_reservation_ui_client import (
    CarChargingReservationUiClient,
)
from system_test.core.clients.system.ui.pages.login_page import LoginPage


def test_frontend_loads_and_renders(
    car_charging_reservation_ui_client: CarChargingReservationUiClient,
):
    """Smoke: Frontend application loads and renders correctly"""
    # Navigate to home - uses client method
    car_charging_reservation_ui_client.navigate_to_home()

    # Assert HTTP response is valid - uses client methods
    car_charging_reservation_ui_client.assert_response_ok()
    car_charging_reservation_ui_client.assert_response_is_html()


def test_ui_redirects_to_login_when_not_authenticated(
    car_charging_reservation_ui_client: CarChargingReservationUiClient,
):
    """Smoke: UI redirects unauthenticated users to login page"""
    # Navigate and get the page we land on - uses client method
    page = car_charging_reservation_ui_client.navigate_to_home()

    # Should be login page
    assert isinstance(page, LoginPage)

    # Verify not authenticated - uses client method
    assert not car_charging_reservation_ui_client.is_authenticated()

    # Verify login page rendered
    page.assert_loaded()


def test_user_can_login_via_ui(
    car_charging_reservation_ui_client: CarChargingReservationUiClient,
):
    """Smoke: Critical path - user can login via UI"""
    # Navigate to login - uses client method
    login_page = car_charging_reservation_ui_client.navigate_to_home()

    # Login
    home_page = login_page.login(username="addisonw", password="addisonwpass")

    # Verify home page loaded
    home_page.assert_loaded()


def test_home_page_loads_with_correct_status_and_content_type(
    car_charging_reservation_ui_client: CarChargingReservationUiClient,
):
    """Smoke: Home page loads with 200 OK and HTML content type"""
    # Navigate - uses client method
    car_charging_reservation_ui_client.navigate_to_home()

    # Check status - uses client method
    status = car_charging_reservation_ui_client.get_response_status()
    assert status == 200, f"Expected 200, got {status}"

    # Check content type - uses client method
    content_type = car_charging_reservation_ui_client.get_response_content_type()
    assert "text/html" in content_type, f"Expected HTML, got {content_type}"


def test_ui_handles_invalid_login(
    car_charging_reservation_ui_client: CarChargingReservationUiClient,
):
    """Smoke: UI properly handles invalid login credentials"""
    # Navigate to login - uses client method
    login_page = car_charging_reservation_ui_client.navigate_to_home()

    # Try invalid login
    login_page.fill_username("invalid_user")
    login_page.fill_password("wrong_password")
    login_page.click_login()

    # Should show error and stay on login page
    login_page.assert_login_failed()
