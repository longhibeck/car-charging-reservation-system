import time

import pytest
import requests


class APIClient:
    """HTTP client wrapper that automatically prepends base URL"""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        return self.session.get(url, **kwargs)

    def post(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        return self.session.post(url, **kwargs)

    def put(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        return self.session.put(url, **kwargs)

    def delete(self, path, **kwargs):
        url = f"{self.base_url}{path}"
        return self.session.delete(url, **kwargs)


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

    return APIClient(api_base_url)
