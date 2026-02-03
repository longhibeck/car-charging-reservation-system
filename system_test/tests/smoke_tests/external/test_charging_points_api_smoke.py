from system_test.core.matchers.result_matchers import to_be_success

def test_should_check_health_successfully(charging_points_api_driver):
    response = charging_points_api_driver.go_to_charging_points()
    to_be_success(response)



def test_should_list_charging_points_successfully(charging_points_api_driver):
    response = charging_points_api_driver.list_charging_points()
    to_be_success(response)