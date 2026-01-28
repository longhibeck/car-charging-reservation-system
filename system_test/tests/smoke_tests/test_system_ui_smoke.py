from system_test.core.matchers.result_matchers import to_be_success


def test_should_be_able_to_go_to_system(system_ui_driver):
    result = system_ui_driver.go_to_system()
    to_be_success(result)


def test_should_be_able_to_login(system_ui_driver):
    result = system_ui_driver.go_to_system()
    to_be_success(result)

    result = system_ui_driver.login("addisonw", "addisonwpass")
    to_be_success(result)

def test_should_be_able_to_list_cars(authenticated_ui_driver):
    result = authenticated_ui_driver.list_cars()
    to_be_success(result)