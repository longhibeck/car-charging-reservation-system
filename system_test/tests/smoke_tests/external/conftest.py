import pytest
from system_test.core.clients.client_factory import ClientFactory


@pytest.fixture()
def auth_api_client():
    return ClientFactory.create_auth_api_client()


@pytest.fixture()
def charging_points_api_client():
    return ClientFactory.create_charging_points_api_client()
