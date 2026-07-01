from system_test.core.drivers.system.commons.dtos.auth_request import LoginRequest
from system_test.core.drivers.system.commons.dtos.auth_response import LoginResponse
from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class LoginVerification(ResponseVerification[LoginResponse]):
    """Domain-specific assertions on a login result.

    Receives the already-unwrapped LoginResponse.
    Add methods here when tests need to inspect the token or user data.
    """

    def has_access_token(self) -> "LoginVerification":
        token = self._response.get("access_token", "")
        assert token, "Expected a non-empty access_token in the login response"
        return self


class Login(BaseUseCase[SystemDriver, LoginResponse, LoginVerification]):
    """Use case: authenticate a user.

    Fluent setters mirror the training PlaceOrder pattern so parameters are
    named at the call-site rather than buried in a request constructor.

    Example
    -------
    app.system().login().username("addisonw").password("pass").execute().should_succeed()
    app.system().login().username("x").password("y").execute().should_fail().error_message("Invalid credentials")
    """

    def __init__(self, driver: SystemDriver, context: UseCaseContext) -> None:
        super().__init__(driver, context)
        self._username: str | None = None
        self._password: str | None = None

    def username(self, value: str) -> "Login":
        self._username = value
        return self

    def password(self, value: str) -> "Login":
        self._password = value
        return self

    def execute(self) -> UseCaseResult[LoginResponse, LoginVerification]:
        request = LoginRequest(
            username=self._username or "",
            password=self._password or "",
        )
        result = self._driver.login(request)
        return UseCaseResult(result, self._context, LoginVerification)
