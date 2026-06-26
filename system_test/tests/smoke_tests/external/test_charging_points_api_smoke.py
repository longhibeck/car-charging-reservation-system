import pytest

from system_test.core.use_case_dsl import UseCaseDsl


class TestChargingPointsApiSmoke:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = UseCaseDsl()
        yield
        self.app.close()

    def test_should_go_to_charging_points(self):
        self.app.charging_points().go_to_charging_points().execute().should_succeed()

    def test_should_list_charging_points_successfully(self):
        self.app.charging_points().list_charging_points().execute().should_succeed()
