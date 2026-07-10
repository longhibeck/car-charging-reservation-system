import pytest

from system_test.core.scenario.impl.scenario_dsl_impl import ScenarioDslImpl
from system_test.core.use_case_dsl import UseCaseDsl


class BaseE2eTest:
    """Base class for all e2e scenario-DSL tests.

    Exposes self.scenario as a field (not a factory method), matching
    the Java reference pattern where tests read as plain-language scenarios:

        self.scenario
            .given().car("car1").exists()
            .when().create_reservation().car_id("car1")
            .then().should_succeed().has_status("active")
    """

    @pytest.fixture(autouse=True)
    def _setup(self):
        app = UseCaseDsl()
        self.scenario = ScenarioDslImpl(app)
        yield
        app.close()
