"""
Smoke tests for the walking skeleton.
These tests verify basic functionality is working.
"""

import pytest


@pytest.mark.smoke
def test_health_endpoint(api_client):
    """Test that the health endpoint returns success"""
    response = api_client.get("/health")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


@pytest.mark.smoke  
def test_root_endpoint(api_client):
    """Test that the root endpoint returns welcome message"""
    response = api_client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert "Car Charging" in data["message"]


# TODO: Add more smoke tests as you implement features
# Example:
# @pytest.mark.smoke
# def test_cars_endpoint_exists(api_client):
#     """Test that cars endpoint exists (even if empty)"""
#     response = api_client.get("/cars")
#     assert response.status_code == 200