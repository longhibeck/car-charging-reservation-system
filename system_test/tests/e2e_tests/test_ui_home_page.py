from system_test.core.clients.system.ui.car_charging_reservation_ui_client import (
    CarChargingReservationUiClient,
)


def test_should_redirect_to_login_when_not_authenticated(
    car_charging_reservation_ui_client: CarChargingReservationUiClient,
):
    """Test unauthenticated user is redirected to login page"""
    login_page = car_charging_reservation_ui_client.navigate_to_home()

    # Verify we're on login page
    login_page.assert_loaded()


def test_should_display_home_page_when_authenticated(
    car_charging_reservation_ui_client: CarChargingReservationUiClient,
):
    """Test authenticated user can access home page"""
    # Login first
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    home_page = login_page.login(username="addisonw", password="addisonwpass")

    # Verify home page loaded
    home_page.assert_loaded()
