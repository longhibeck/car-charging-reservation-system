from system_test.core.clients.client_factory import ClientFactory
from playwright.sync_api import Page
import pytest


@pytest.fixture
def car_charging_reservation_ui_client(page: Page):
    yield ClientFactory.create_car_charging_reservation_ui_client(page)
