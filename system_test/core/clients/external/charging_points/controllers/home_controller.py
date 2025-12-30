from system_test.core.clients.commons.http_test_client import HttpTestClient


class HomeController:
    ENDPOINT = "/"

    def __init__(self, http_client: HttpTestClient):
        self.http_client = http_client

    def get_home(self):
        return self.http_client.get(HomeController.ENDPOINT)

    def assert_get_home_succesful(self, response):
        self.http_client.assert_ok(response)
