from system_test.core.matchers.result_matchers import to_be_success, to_be_failure_with

def test_should_go_to_auth(auth_api_driver):
    response = auth_api_driver.go_to_auth()
    to_be_success(response)


def test_should_not_login_with_invalid_credentials(auth_api_driver):
    response = auth_api_driver.login("test", "123")
    to_be_failure_with(response, "Invalid credentials")