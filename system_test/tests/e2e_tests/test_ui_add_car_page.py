from system_test.core.matchers.result_matchers import to_be_success


def test_should_add_car(authenticated_ui_driver):
    result = authenticated_ui_driver.add_car(
        name="Test Car",
        connector_types=["Type 2"],
        battery_charge_limit="80",
        battery_size="60",
        max_kw_ac="11",
        max_kw_dc="50",
    )
    to_be_success(result)


def test_should_add_car_with_multiple_connectors(authenticated_ui_driver):
    result = authenticated_ui_driver.add_car(
        name="Test Car",
        connector_types=["Type 2", "CCS", "Schuko"],
        battery_charge_limit="80",
        battery_size="60",
        max_kw_ac="11",
        max_kw_dc="50",
    )
    to_be_success(result)
