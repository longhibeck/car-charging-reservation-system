from system_test.core.drivers.driver_factory import DriverFactory
from system_test.core.drivers.commons.result_assert import ResultAssert


class TestChargingPointsApiSmoke:
    driver = DriverFactory.create_charging_points_api_driver()

    def test_should_go_to_charging_points(self):
        result = self.driver.go_to_charging_points()
        ResultAssert.assert_that_result(result).is_success()

    def test_should_list_charging_points_successfully(self):
        result = self.driver.list_charging_points()
        ResultAssert.assert_that_result(result).is_success()
