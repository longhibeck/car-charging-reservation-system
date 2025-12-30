def test_should_get_home(charging_points_api_client):
    response = charging_points_api_client.home().get_home()
    charging_points_api_client.home().assert_get_home_succesful(response)


def test_should_get_charging_points(charging_points_api_client):
    response = charging_points_api_client.charging_points().get_charging_points()
    charging_points_api_client.charging_points().assert_get_charging_points_successful(response)
