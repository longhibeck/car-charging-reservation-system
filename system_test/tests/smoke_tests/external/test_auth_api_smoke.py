from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.drivers.driver_factory import DriverFactory


class TestAuthApiSmoke:
    driver = DriverFactory.create_auth_api_driver()

    def test_should_go_to_auth(self):
        result = self.driver.go_to_auth()
        ResultAssert.assert_that_result(result).is_success()

    def test_should_not_login_with_invalid_credentials(self):
        result = self.driver.login("test", "123")
        ResultAssert.assert_that_result(result).is_failure("Invalid credentials")
