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

    assert response.status_code != 404
    assert response.status_code in [200, 401, 422]


def test_core_business_endpoint_exists(api_client):
    """Test that core business endpoint (cars) exists and responds"""
    response = api_client.get("/api/v1/cars/")

    assert response.status_code != 404
    assert response.status_code in [200, 401, 403]


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
