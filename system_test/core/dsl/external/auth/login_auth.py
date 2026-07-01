from system_test.core.drivers.external.auth.auth_driver import AuthDriver
from system_test.core.drivers.external.auth.dtos.login_request import LoginRequest
from system_test.core.drivers.external.auth.dtos.login_response import LoginResponse
from system_test.core.dsl.shared.base_use_case import BaseUseCase
from system_test.core.dsl.shared.response_verification import ResponseVerification
from system_test.core.dsl.shared.use_case_context import UseCaseContext
from system_test.core.dsl.shared.use_case_result import UseCaseResult


class AuthLoginVerification(ResponseVerification[LoginResponse]):
    """Assertions on an external auth login result.

    Example
    -------
    .execute().should_succeed().has_access_token()
    """

    def has_access_token(self) -> "AuthLoginVerification":
        token = self._response.get("accessToken", "")
        assert token, "Expected a non-empty accessToken in the auth login response"
        return self


class LoginAuth(BaseUseCase[AuthDriver, LoginResponse, AuthLoginVerification]):
    """Use case: authenticate against the external auth service.

    Example
    -------
    app.auth().login().username("addisonw").password("pass").execute().should_succeed()
    app.auth().login().username("x").password("y").execute().should_fail().error_message("Invalid credentials")
    """

    def __init__(self, driver: AuthDriver, context: UseCaseContext) -> None:
        super().__init__(driver, context)
        self._username: str | None = None
        self._password: str | None = None

    def username(self, value: str) -> "LoginAuth":
        self._username = value
        return self

    def password(self, value: str) -> "LoginAuth":
        self._password = value
        return self

    def execute(self) -> UseCaseResult[LoginResponse, AuthLoginVerification]:
        request = LoginRequest(
            username=self._username or "",
            password=self._password or "",
        )
        result = self._driver.login(request)
        return UseCaseResult(result, self._context, AuthLoginVerification)
