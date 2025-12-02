import pytest

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
    car = response.json()
    assert car["id"] is not None
    assert car["name"] == "BYD Seal U"
    assert car["connector_types"] == ["CCS"]
    assert car["battery_charge_limit"] == 100
    assert car["battery_size"] == 87
    assert car["max_kw_ac"] == 11
    assert car["max_kw_dc"] == 150

def test_should_update_car(logged_in_api_context):
    data = {
        "name": "BYD Seal U",
        "connector_types": ["CCS"],
        "battery_charge_limit": 100,
        "battery_size": 87,
        "max_kw_ac": 11,
        "max_kw_dc": 150,
    }
    create_response = logged_in_api_context.post("/api/v1/cars/", data=data)
    assert create_response.status == 201
    created_car = create_response.json()
    car_id = created_car["id"]
    updated_data = {
        "name": "BYD Seal",
        "connector_types": ["Type-2"],
        "battery_charge_limit": 80,
        "battery_size": 87,
        "max_kw_ac": 11,
        "max_kw_dc": 150,
    }
    update_response = logged_in_api_context.put(f"/api/v1/cars/{car_id}", data=updated_data)
    assert update_response.status == 200
    updated_car = update_response.json()
    assert updated_car["id"] == car_id
    assert updated_car["name"] == "BYD Seal"
    assert updated_car["connector_types"] == ["Type-2"]
    assert updated_car["battery_charge_limit"] == 80

def test_should_get_car(logged_in_api_context):
    data = {
        "name": "BYD Seal U",
        "connector_types": ["CCS"],
        "battery_charge_limit": 100,
        "battery_size": 87,
        "max_kw_ac": 11,
        "max_kw_dc": 150,
    }
    create_response = logged_in_api_context.post("/api/v1/cars/", data=data)
    assert create_response.status == 201
    created_car = create_response.json()
    car_id = created_car["id"]
    get_response = logged_in_api_context.get(f"/api/v1/cars/{car_id}")
    assert get_response.status == 200
    car = get_response.json()
    assert car["id"] == car_id
    assert car["name"] == "BYD Seal U"
    assert car["connector_types"] == ["CCS"]
    assert car["battery_charge_limit"] == 100
    assert car["battery_size"] == 87
    assert car["max_kw_ac"] == 11
    assert car["max_kw_dc"] == 150

@pytest.mark.parametrize("value", (0,120,-10))
def test_should_not_create_car_with_invalid_battery_charge_limit(logged_in_api_context, value):
    data = {
        "name": "BYD Seal U",
        "connector_types": ["CCS"],
        "battery_charge_limit": value,
        "battery_size": 87,
        "max_kw_ac": 11,
        "max_kw_dc": 150,
    }
    response = logged_in_api_context.post("/api/v1/cars/", data=data)
    assert response.status == 422
    error_data = response.json()
    assert "detail" in error_data
    error_message = str(error_data)
    assert "battery_charge_limit" in error_message.lower()



def test_should_not_create_car_with_data_type(logged_in_api_context, ):
    data = {
        "name": "BYD Seal U",
        "connector_types": ["CCS"],
        "battery_charge_limit": 100,
        "battery_size": "not_a_number",
        "max_kw_ac": 11,
        "max_kw_dc": 150,
    }
    response = logged_in_api_context.post("/api/v1/cars/", data=data)
    assert response.status == 422
    error_data = response.json()
    assert "detail" in error_data
    error_message = str(error_data)
    assert "battery_size" in error_message.lower()