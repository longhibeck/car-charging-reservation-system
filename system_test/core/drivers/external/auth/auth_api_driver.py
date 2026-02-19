from system_test.core.drivers.external.auth.client.auth_api_client import AuthApiClient
from system_test.core.drivers.commons.clients.http_test_client import HttpTestClient
from system_test.core.drivers.commons.clients.closer import Closer
from httpx import Client


class AuthApiDriver:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self._http_client = Client(base_url=base_url, headers={"Content-Type": "application/json"})
        http_test_client = HttpTestClient(self._http_client, base_url)
        self._api_client = AuthApiClient(http_test_client)

    def go_to_auth(self):
        return self._api_client.health().check_health()

    def login(self, username: str, password: str):
        return self._api_client.auth().login(username, password)
    
    def close(self) -> None:
        Closer.close(self._http_client)
