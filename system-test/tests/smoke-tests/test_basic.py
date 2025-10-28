def test_health_endpoint(api_client):
    """Test that the health endpoint returns success"""
    response = api_client.get("/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_root_endpoint(api_client):
    """Test that the root endpoint returns the dashboard or redirects to login"""
    response = api_client.get("/", allow_redirects=False)

    # Accept either dashboard HTML or redirect to login if not authenticated
    if response.status_code in (302, 307):
        # Should redirect to /login
        assert "/login" in response.headers.get("location", "")
    else:
        assert response.status_code == 200
        # Should return HTML dashboard page
        assert (
            "<title>Main Dashboard</title>" in response.text
            or "Welcome" in response.text
        )


def test_root_endpoint_exists(api_client):
    """Test that car endpoint exists"""
    response = api_client.get("/")
    assert response.status_code == 200


def test_login_endpoint_exists(api_client):
    """Test that login endpoint exists"""
    response = api_client.get("/login")
    assert response.status_code == 200


def test_car_endpoint_exists(api_client):
    """Test that car endpoint exists"""
    response = api_client.get("/car")
    assert response.status_code == 200


def test_car_add_endpoint_exists(api_client):
    """Test that car endpoint exists"""
    response = api_client.get("/car/add")
    assert response.status_code == 200
