import pytest
import httpx

@pytest.fixture(scope="session")
def api_client(base_url):
    """An httpx client configured with the base URL."""
    with httpx.Client(
        base_url=base_url,
        timeout=30.0,
        follow_redirects=True,
    ) as client:
        yield client