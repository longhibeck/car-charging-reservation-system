from system_test.core.matchers.result_matchers import to_be_success


def test_should_redirect_to_login_when_not_authenticated(system_ui_driver):
    result = system_ui_driver.go_to_system()
    to_be_success(result)
