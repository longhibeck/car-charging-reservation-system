
def test_should_get_charging_points(charging_points_api_context):
    response = charging_points_api_context.get("/api/v1/charging-points")

    assert response.status == 200
    assert "application/json" in response.headers.get("content-type", "")

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_should_check_first_charging_point(charging_points_api_context):
    response = charging_points_api_context.get("/api/v1/charging-points/550e8400-e29b-41d4-a716-446655440001")

    assert response.status == 200

    data = response.json()
    assert data["id"] == "550e8400-e29b-41d4-a716-446655440001"
    assert data["name"] == "CP-001"
    assert data["status"] == "available"
    assert data["connector_type"] == "Type 2"
    assert data["charging_type"] == "AC"
    assert data["max_power_kw"] == 22

    