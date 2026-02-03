from system_test.core.matchers.result_matchers import to_be_success, to_be_failure_with


def test_should_display_home_page_when_authenticated(
    authenticated_ui_driver,
):
    result = authenticated_ui_driver.go_to_system()
    to_be_success(result)


def test_should_not_login_with_invalid_credentials(system_ui_driver):
    result = system_ui_driver.login("invalid_user", "invalid_pass")
    to_be_failure_with(result, "Login failed")
