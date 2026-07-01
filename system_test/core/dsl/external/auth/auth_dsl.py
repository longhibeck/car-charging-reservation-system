from system_test.core.drivers.external.auth.auth_driver import AuthDriver
from system_test.core.dsl.external.auth.go_to_auth import GoToAuth
from system_test.core.dsl.external.auth.login_auth import LoginAuth
from system_test.core.dsl.shared.use_case_context import UseCaseContext


class AuthDsl:
    """Domain DSL for the external auth service.

    One factory method per use case — no logic here, only creation.

    Example
    -------
    app.auth().go_to_auth().execute().should_succeed()
    app.auth().login().username("addisonw").password("pass").execute().should_succeed()
    """

    def __init__(self, driver: AuthDriver, context: UseCaseContext) -> None:
        self._driver = driver
        self._context = context

    def go_to_auth(self) -> GoToAuth:
        return GoToAuth(self._driver, self._context)

    def login(self) -> LoginAuth:
        return LoginAuth(self._driver, self._context)

    def close(self) -> None:
        self._driver.close()
