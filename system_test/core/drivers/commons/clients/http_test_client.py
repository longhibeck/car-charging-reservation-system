from typing import TypeVar, Any
from system_test.core.drivers.commons.clients.typed_response import TypedResponse
import httpx

T = TypeVar("T")


class HttpTestClient:
    def __init__(self, client: httpx.Client, base_url: str):
        self.client = client
        self.base_url = base_url

    def get(self, path: str) -> TypedResponse[T]:
        return self.client.get(path)

    def post(self, path: str, body: Any) -> TypedResponse[T]:
        return self.client.post(path, json=body)

    def put(self, path: str, body: Any) -> TypedResponse[T]:
        return self.client.put(path, json=body)

    def delete(self, path: str) -> TypedResponse[T]:
        return self.client.delete(path)
