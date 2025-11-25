def test_should_login(api_request_context):
    data = {"username": "addisonw", "password": "addisonwpass"}
    response = api_request_context.post("/api/v1/auth/login", data=data)
    response_json = response.json()
    assert response.ok
    assert response_json["token"] is not None
    assert response_json["user"]["id"] is not None
    assert response_json["user"]["username"] == "addisonw"
    assert response_json["user"]["external_user_id"] is not None


def test_should_should_display_current_user(logged_in_api_context):
    response = logged_in_api_context.get("/api/v1/auth/me")
    response_json = response.json()
    assert response.ok
    assert response_json["id"] is not None
    assert response_json["username"] == "addisonw"
    assert response_json["external_user_id"] > 0
