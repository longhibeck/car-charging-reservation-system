from system_test.core.clients.system.ui.car_charging_reservation_ui_client import CarChargingReservationUiClient


def test_should_navigate_to_add_car_page(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test user can navigate from cars page to add car page"""
    # Login
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    home_page = login_page.login(username="addisonw", password="addisonwpass")
    
    # Navigate to cars page
    cars_page = home_page.click_view_all_cars()
    cars_page.assert_loaded()
    
    # Click Add Car button
    add_car_page = cars_page.click_add_car()
    
    # Verify we're on add car page
    add_car_page.assert_loaded()


def test_should_display_cars_page_when_authenticated(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test authenticated user can view cars page"""
    # Login
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    home_page = login_page.login(username="addisonw", password="addisonwpass")
    
    # Navigate to cars page
    cars_page = home_page.click_view_all_cars()
    
    # Verify cars page loaded
    cars_page.assert_loaded()