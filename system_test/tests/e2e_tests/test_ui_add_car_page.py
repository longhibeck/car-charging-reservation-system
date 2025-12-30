from system_test.core.clients.system.ui.car_charging_reservation_ui_client import CarChargingReservationUiClient


def test_should_add_car(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test user can add a new car"""
    # Login
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    home_page = login_page.login(username="addisonw", password="addisonwpass")
    
    # Navigate to add car page
    cars_page = home_page.click_view_all_cars()
    add_car_page = cars_page.click_add_car()
    
    # Add car using composite method
    cars_page = add_car_page.add_car(
        name="Test Car",
        connector_type_2=True,
        battery_charge_limit="80",
        battery_size="60",
        max_kw_ac="11",
        max_kw_dc="50"
    )
    
    # Verify car was added
    cars_page.assert_car_in_table(
        car_name="Test Car",
        battery_size="60",
        max_kw_ac="11",
        max_kw_dc="50"
    )


def test_should_validate_missing_car_name(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test form validation when car name is missing"""
    # Login
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    home_page = login_page.login(username="addisonw", password="addisonwpass")
    
    # Navigate to add car page
    cars_page = home_page.click_view_all_cars()
    add_car_page = cars_page.click_add_car()
    
    # Fill form WITHOUT car name
    add_car_page.select_connector_type_2()
    add_car_page.fill_battery_charge_limit("80")
    add_car_page.fill_battery_size("60")
    add_car_page.fill_max_kw_ac("11")
    add_car_page.fill_max_kw_dc("50")
    
    # Try to submit
    add_car_page.click_add_car()
    
    # Verify validation message (stays on add car page)
    validation_message = add_car_page.get_car_name_validation_message()
    assert validation_message != "", "Expected validation message for missing car name"
    
    # Still on add car page
    add_car_page.assert_loaded()


def test_should_add_car_with_multiple_connectors(car_charging_reservation_ui_client: CarChargingReservationUiClient):
    """Test user can add a car with multiple connector types"""
    # Login
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    home_page = login_page.login(username="addisonw", password="addisonwpass")
    
    # Navigate to add car page
    cars_page = home_page.click_view_all_cars()
    add_car_page = cars_page.click_add_car()
    
    # Add car with multiple connectors
    cars_page = add_car_page.add_car(
        name="Multi Connector Car",
        connector_type_2=True,
        connector_ccs=True,
        battery_charge_limit="90",
        battery_size="75",
        max_kw_ac="22",
        max_kw_dc="150"
    )
    
    # Verify car was added
    cars_page.assert_car_in_table(
        car_name="Multi Connector Car",
        battery_size="75",
        max_kw_ac="22",
        max_kw_dc="150"
    )
