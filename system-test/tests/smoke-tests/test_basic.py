import httpx
import pytest

def test_system_health_check(api_client):
    """Test that the system health endpoint is responding"""
    response = api_client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_auth_endpoint_exists(api_client):
    """Test that authentication endpoint exists and responds"""
    response = api_client.post(
        "/api/v1/auth/login",
        json={"username": "addisonw", "password": "addisonwpass"},
    )

    assert response.status_code in [200, 401, 422]


def test_core_business_endpoint_exists(api_client):
    """Test that core business endpoint (cars) exists and responds"""
    response = api_client.get("/api/v1/cars/")

    assert response.status_code == 401


def test_frontend_loads(api_client):
    """Test that the frontend application loads successfully"""
    response = api_client.get("/")

    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    assert "<title>Car Charging Reservation System</title>" in response.text


def test_frontend_assets_accessible(api_client):
    """Test that essential frontend assets are accessible"""
    css_response = api_client.get("/css/styles.css")
    assert css_response.status_code == 200

    js_response = api_client.get("/js/app.js")
    assert js_response.status_code == 200


def test_auth_external_api():
    """Test that the external auth system (DummyJSON) is up"""
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.post(
                "https://dummyjson.com/auth/login",
                json={"username": "ping", "password": "ping"},
            )

            assert response.status_code != 503, "DummyJSON API is unreachable"
            assert response.status_code != 500, "DummyJSON API returned server error"
            assert response.status_code in [200, 400, 401], (
                f"Unexpected response from DummyJSON: {response.status_code}"
            )

    except httpx.ConnectTimeout:
        pytest.fail("DummyJSON API is unreachable (timeout)")
    except httpx.ConnectError:
        pytest.fail("DummyJSON API is unreachable (connection error)")
    except httpx.RequestError as e:
        pytest.fail(f"DummyJSON API request failed: {e}")


def test_auth_backend_integration(api_client):
    """Test that our backend can integrate with the external auth system"""
    response = api_client.post(
        "/api/v1/auth/login",
        json={"username": "ping", "password": "ping"},
    )
    
    # Any response other than 503/500 means our backend can reach the external service
    assert response.status_code != 503, "Backend cannot reach external auth API"
    assert response.status_code != 500, "Backend error when calling external auth API"