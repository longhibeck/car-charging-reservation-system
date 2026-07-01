from typing import Any

import httpx

from system_test.core.drivers.commons.clients.typed_response import TypedResponse


class HttpTestClient:
    def __init__(self, client: httpx.Client, base_url: str):
        self.client = client
        self.base_url = base_url

    def get[T](self, path: str) -> TypedResponse[T]:
        return TypedResponse(self.client.get(path))

    def post[T](self, path: str, body: Any) -> TypedResponse[T]:
        return TypedResponse(self.client.post(path, json=body))

    def put[T](self, path: str, body: Any) -> TypedResponse[T]:
        return TypedResponse(self.client.put(path, json=body))

    def delete[T](self, path: str) -> TypedResponse[T]:
        return TypedResponse(self.client.delete(path))
