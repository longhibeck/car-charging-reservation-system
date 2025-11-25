def test_should_list_cars(logged_in_api_context):
    response = logged_in_api_context.get("/api/v1/cars/")
    assert response.ok
    response_json = response.json()
    assert response_json == {"cars": []}


def test_should_create_car(logged_in_api_context):
    data = {
        "name": "BYD Seal U",
        "connector_types": ["CCS"],
        "battery_charge_limit": 100,
        "battery_size": 87,
        "max_kw_ac": 11,
        "max_kw_dc": 150,
    }
    response = logged_in_api_context.post("/api/v1/cars/", data=data)
    assert response.status == 201
    response_json = response.json()
    assert response_json["id"] is not None
    assert response_json["name"] == "BYD Seal U"
    assert response_json["connector_types"] == ["CCS"]
    assert response_json["battery_charge_limit"] == 100
    assert response_json["battery_size"] == 87
    assert response_json["max_kw_ac"] == 11
    assert response_json["max_kw_dc"] == 150
