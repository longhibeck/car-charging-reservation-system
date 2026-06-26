import pytest

from system_test.core.use_case_dsl import UseCaseDsl


class TestAuthApiSmoke:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = UseCaseDsl()
        yield
        self.app.close()

    def test_should_go_to_auth(self):
        self.app.auth().go_to_auth().execute().should_succeed()

    def test_should_not_login_with_invalid_credentials(self):
        (
            self.app.auth()
            .login()
            .username("test")
            .password("123")
            .execute()
            .should_fail()
            .error_message("Invalid credentials")
        )
