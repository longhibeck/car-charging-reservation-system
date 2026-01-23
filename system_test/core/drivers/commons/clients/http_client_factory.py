from httpx import Client


class HttpClientFactory:
    @staticmethod
    def create(base_url: str) -> Client:
        return Client(base_url=base_url, headers={"Content-Type": "application/json"})
