from system_test.core.matchers.result_matchers import to_be_success


def test_should_display_cars_page_when_authenticated(authenticated_ui_driver):
    result = authenticated_ui_driver.list_cars()
    to_be_success(result)
