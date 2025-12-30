def test_should_get_health_endpoint(car_charging_reservation_api_client):
    """Smoke test: Verify the service is up and healthy (no auth required)"""
    response = car_charging_reservation_api_client.health().get_health()
    car_charging_reservation_api_client.health().assert_healthy(response)


def test_should_list_cars(car_charging_reservation_api_client):
    """Smoke test: Verify cars endpoint is accessible"""
    response = car_charging_reservation_api_client.cars().list_cars()
    car_charging_reservation_api_client.cars().assert_unauthenticated_access_denied(
        response
    )


def test_should_list_reservations(car_charging_reservation_api_client):
    """Smoke test: Verify reservations endpoint is accessible"""
    response = car_charging_reservation_api_client.reservations().list_reservations()
    car_charging_reservation_api_client.reservations().assert_unauthenticated_access_denied(
        response
    )


def test_should_login(car_charging_reservation_api_client):
    """Smoke test: Verify authentication is working"""
    response = car_charging_reservation_api_client.auth().login(
        username="addisonw", password="addisonwpass"
    )
    car_charging_reservation_api_client.auth().assert_login_successful(response)
