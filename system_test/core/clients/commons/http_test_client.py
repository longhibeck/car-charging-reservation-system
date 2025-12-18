import httpx
from http import HTTPStatus


class HttpTestClient:
    def __init__(self, base_url: str):
        self.client = httpx.Client(
            base_url=base_url,
            headers={"Content-Type": "application/json"},
            follow_redirects=True,
            verify=False
        )

    def get(self, path: str) -> httpx.Response:
        return self.client.get(path)

    def post(self, path: str, request_body: dict | None = None) -> httpx.Response:
        return self.client.post(path, json=request_body)

    def assert_ok(self, response: httpx.Response) -> None:
        self._assert_status(response, HTTPStatus.OK)

    def assert_created(self, response: httpx.Response) -> None:
        self._assert_status(response, HTTPStatus.CREATED)

    def assert_no_content(self, response: httpx.Response) -> None:
        self._assert_status(response, HTTPStatus.NO_CONTENT)

    def assert_unprocessable_entity(self, response: httpx.Response) -> None:
        self._assert_status(response, HTTPStatus.UNPROCESSABLE_ENTITY)

    def assert_unauthorized(self, response: httpx.Response) -> None:
        self._assert_status(response, HTTPStatus.UNAUTHORIZED)
    
    def assert_bad_request(self, response: httpx.Response) -> None:
        """Assert response is 400 Bad Request"""
        self._assert_status(response, HTTPStatus.BAD_REQUEST)

    def _assert_status(self, response: httpx.Response, expected_status: int) -> None:
        if response.status_code != expected_status:
            body_text = response.text
            raise AssertionError(
                f"Expected status {expected_status} but got {response.status_code}. "
                f"Response body: {body_text}"
            )

    def read_body(self, response: httpx.Response) -> dict:
        return response.json()
