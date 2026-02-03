from system_test.core.matchers.result_matchers import to_be_success, to_be_failure_with


def test_should_login_with_valid_credentials(system_api_driver) -> None:
    result = system_api_driver.login(username="addisonw", password="addisonwpass")
    to_be_success(result)


def test_should_fail_login_with_invalid_credentials(system_api_driver) -> None:
    result = system_api_driver.login(username="invaliduser", password="wrongpass")
    to_be_failure_with(result, "Invalid credentials")


def test_should_get_current_user(system_api_driver) -> None:
    login_result = system_api_driver.login(username="addisonw", password="addisonwpass")
    to_be_success(login_result)
    current_user_result = system_api_driver.get_current_user()
    to_be_success(current_user_result)
