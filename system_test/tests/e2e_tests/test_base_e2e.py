from abc import ABC, abstractmethod
import pytest
from system_test.core.drivers.commons.result_assert import ResultAssert
from system_test.core.drivers.driver_factory import DriverFactory
from functools import wraps


def login_as(username: str = "addisonw", password: str = "addisonwpass"):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = self.system_driver.login(username, password)
            ResultAssert.assert_that_result(result).is_success()
            return func(self, *args, **kwargs)

        return wrapper

    return decorator


class BaseE2eTest(ABC):
    @abstractmethod
    def create_system_driver(self): ...

    @pytest.fixture(autouse=True)
    def setup(self):
        self.system_driver = self.create_system_driver()
        self.charging_points_api_driver = (
            DriverFactory.create_charging_points_api_driver()
        )
        self.auth_api_driver = DriverFactory.create_auth_api_driver()
        yield
        self.system_driver.close()
        self.charging_points_api_driver.close()
        self.auth_api_driver.close()

    def test_should_login(self) -> None:
        result = self.system_driver.login("addisonw", "addisonwpass")
        ResultAssert.assert_that_result(result).is_success()

    def test_should_not_login_with_invalid_credentials(self) -> None:
        result = self.system_driver.login("invalid_user", "invalid_pass")
        ResultAssert.assert_that_result(result).is_failure("Invalid credentials")

    @login_as()
    def test_should_add_car(self) -> None:
        add_car_result = self.system_driver.add_car(
            name="BYD Seal U",
            connector_types=["CCS"],
            battery_charge_limit=100,
            battery_size=87,
            max_kw_ac=11,
            max_kw_dc=15,
        )
        ResultAssert.assert_that_result(add_car_result).is_success()

    @pytest.mark.parametrize(
        "connector_types",
        [
            (["Type 2", "Schuko"]),
            (["Type 2", "CCS"]),
            (["Type 2", "CCS", "Schuko"]),
        ],
    )
    @login_as()
    def test_should_add_car_with_multiple_valid_connector_types(self, connector_types) -> None:
        add_car_result = self.system_driver.add_car(
            name="BYD Seal U",
            connector_types=connector_types,
            battery_charge_limit=100,
            battery_size=87,
            max_kw_ac=11,
            max_kw_dc=15,
        )
        ResultAssert.assert_that_result(add_car_result).is_success()

    @login_as()
    def test_should_list_cars(self) -> None:
        list_cars_result = self.system_driver.list_cars()
        ResultAssert.assert_that_result(list_cars_result).is_success()

    @pytest.mark.parametrize("value", (0, -10, -20))
    @login_as()
    def test_should_not_create_car_with_zero_or_negative_battery_charge_limit(
        self, value
    ) -> None:
        add_car_result = self.system_driver.add_car(
            name="Invalid Car",
            connector_types=["CCS"],
            battery_charge_limit=value,
            battery_size=87,
            max_kw_ac=11,
            max_kw_dc=15,
        )
        ResultAssert.assert_that_result(add_car_result).is_failure(
            "Input should be greater than 0"
        )

    @pytest.mark.parametrize("value", (101, 200, 150))
    @login_as()
    def test_should_not_create_car_with_over_hundred_battery_charge_limit(self, value) -> None:
        add_car_result = self.system_driver.add_car(
            name="Invalid Car",
            connector_types=["CCS"],
            battery_charge_limit=value,
            battery_size=87,
            max_kw_ac=11,
            max_kw_dc=15,
        )
        ResultAssert.assert_that_result(add_car_result).is_failure(
            "Input should be less than or equal to 100"
        )
