from system_test.core.drivers.external.auth.client.auth_api_client import AuthApiClient


class AuthApiDriver:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self._api_client = AuthApiClient(base_url)

    def go_to_auth(self):
        return self._api_client.health().check_health()

    def login(self, username: str, password: str):
        return self._api_client.auth().login(username, password)
