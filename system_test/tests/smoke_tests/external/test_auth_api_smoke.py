from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.external.auth.dtos.login_request import LoginRequest


class TestAuthApiSmoke:
    driver = DriverFactory.create_auth_api_driver()

    def test_should_go_to_auth(self):
        result = self.driver.go_to_auth()
        ResultAssert.assert_that_result(result).is_success()

    def test_should_not_login_with_invalid_credentials(self):
        request = LoginRequest(username="test", password="123")
        result = self.driver.login(request)
        ResultAssert.assert_that_result(result).is_failure("Invalid credentials")
