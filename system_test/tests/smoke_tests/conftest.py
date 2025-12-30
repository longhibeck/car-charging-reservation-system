from system_test.core.clients.client_factory import ClientFactory
from playwright.sync_api import Page
import pytest


@pytest.fixture
def car_charging_reservation_ui_client(page: Page):
    return ClientFactory.create_car_charging_reservation_ui_client(page)


@pytest.fixture
def car_charging_reservation_api_client():
    """Fixture that provides an authenticated API client for smoke tests"""
    return ClientFactory.create_car_charging_reservation_api_client()


@pytest.fixture
def authenticated_api_client(car_charging_reservation_api_client):
    """Fixture that provides an authenticated API client for smoke tests"""

    # Login to get auth token
    login_response = car_charging_reservation_api_client.auth().login(
        "addisonw", "addisonwpass"
    )
    login_data = car_charging_reservation_api_client.auth().assert_login_successful(
        login_response
    )

    # Set auth token for subsequent requests
    car_charging_reservation_api_client.set_auth_token(login_data["access_token"])

    return car_charging_reservation_api_client
