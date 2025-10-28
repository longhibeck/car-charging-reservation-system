import time

import pytest
import requests


@pytest.fixture(scope="session")
def api_base_url():
    """Base URL for the API"""
    return "http://localhost:8080"


@pytest.fixture(scope="session")
def api_client(api_base_url):
    """HTTP client for API testing"""
    # Wait for the service to be ready
    max_attempts = 30
    for _ in range(max_attempts):
        try:
            response = requests.get(f"{api_base_url}/health", timeout=1)
            if response.status_code == 200:
                break
        except requests.exceptions.RequestException:
            time.sleep(1)
    else:
        pytest.fail("Service did not start within expected time")

    session = requests.Session()
    session.base_url = api_base_url

    # Helper method to make requests with base URL
    def request_with_base_url(method, path, **kwargs):
        url = f"{api_base_url}{path}"
        return session.request(method, url, **kwargs)

    session.get = lambda path, **kwargs: request_with_base_url("GET", path, **kwargs)
    session.post = lambda path, **kwargs: request_with_base_url("POST", path, **kwargs)
    session.put = lambda path, **kwargs: request_with_base_url("PUT", path, **kwargs)
    session.delete = lambda path, **kwargs: request_with_base_url(
        "DELETE", path, **kwargs
    )

    return session
