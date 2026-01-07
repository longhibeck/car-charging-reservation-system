def test_should_get_home(auth_api_client):
    response = auth_api_client.home().get_home()
    auth_api_client.home().assert_get_home_succesful(response)


def test_should_not_login_with_invalid_credentials(auth_api_client):
    response = auth_api_client.login().post_login("test", "123")
    auth_api_client.login().assert_login_failed(response)
