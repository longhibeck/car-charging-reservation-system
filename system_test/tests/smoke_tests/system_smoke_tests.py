from system_test.core.matchers.result_matchers import to_be_success


def test_should_be_able_to_go_to_system(system_api_driver):
    result = system_api_driver.go_to_system()
    to_be_success(result)


def test_should_be_able_to_login(system_api_driver):
    result = system_api_driver.login("addisonw", "addisonwpass")
    to_be_success(result)

def test_should_be_able_to_list_reservations(authenticated_api_driver):
    result = authenticated_api_driver.list_reservations()
    to_be_success(result)


def test_should_be_able_to_list_cars(authenticated_api_driver):
    result = authenticated_api_driver.list_cars()
    to_be_success(result)
