from system_test.core.drivers.system.system_driver import SystemDriver
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.system.reservation_system.ui.client.system_ui_client import (
    SystemUiClient,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.home_page import (
    HomePage,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.login_page import (
    LoginPage,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.cars_page import (
    CarsPage,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.add_car_page import (
    AddCarPage,
)
from system_test.core.drivers.system.commons.dtos.car_response import (
    AddCarResponse,
)
from enum import StrEnum


class Pages(StrEnum):
    NONE = "none"
    CARS = "cars"
    ADD_CAR = "add_car"
    HOME = "home"
    LOGIN = "login"


class SystemUiDriver(SystemDriver):
    def __init__(self, base_url: str) -> None:
        self._client = SystemUiClient(base_url)
        self._page_client = None  # NOT HAPPY WITH IT
        self._current_page: Pages = Pages.NONE
        self._home_page: HomePage = None
        self._login_page: LoginPage = None
        self._cars_page: CarsPage = None
        self._add_car_page: AddCarPage = None

    def go_to_system(self) -> Result[None]:
        self._page_client = self._client.navigate_to_base()

        if not self._client.is_status_ok() or not self._client.is_page_loaded():
            return Result.failure("Failed to load system page")

        self._detect_current_page()
        return Result.success()

    def login(self, username: str, password: str) -> Result[None]:
        self.ensure_on_login_page()
        self._login_page.input_username(username)
        self._login_page.input_password(password)
        self._login_page.click_login()
        self._page_client.get_page().wait_for_load_state("networkidle")

        self._detect_current_page()

        if self._current_page != Pages.HOME:
            error_message = self._login_page.get_error_message()
            if error_message:
                return Result.failure(error_message)
            return Result.failure("Login failed - still on login page")

        return Result.success()

    def add_car(
        self,
        name: str,
        connector_types: list[str],
        battery_charge_limit: int,
        battery_size: int,
        max_kw_ac: int,
        max_kw_dc: int,
    ) -> Result[AddCarResponse]:
        self.ensure_on_cars_page()
        self._add_car_page = self._cars_page.click_add_car()

        self._add_car_page.input_car_name(name)
        self._add_car_page.input_battery_charge_limit(str(battery_charge_limit))
        self._add_car_page.input_battery_size(str(battery_size))
        self._add_car_page.input_max_kw_ac(str(max_kw_ac))
        self._add_car_page.input_max_kw_dc(str(max_kw_dc))

        for connector_type in connector_types:
            if connector_type == "Type 2":
                self._add_car_page.check_connector_type_2()
            elif connector_type == "CCS":
                self._add_car_page.check_connector_ccs()
            elif connector_type == "CHAdeMO":
                self._add_car_page.check_connector_chademo()
            elif connector_type == "Schuko":
                self._add_car_page.check_connector_schuko()

        self._cars_page = self._add_car_page.click_add_car()
        self._current_page = Pages.CARS

        return Result.success()

    def list_cars(self) -> Result[list]:
        self.ensure_on_cars_page()
        return Result.success()

    def ensure_on_login_page(self) -> None:
        if self._current_page != Pages.LOGIN:
            self._page_client = self._client.navigate_to_base()
            self._detect_current_page()

            if self._current_page != Pages.LOGIN:
                raise Exception("Expected to land on login page but didn't")

    def ensure_on_cars_page(self) -> None:
        """Ensure we're on cars page"""
        if self._current_page != Pages.CARS:
            self._page_client = self._client.navigate_to_base()
            self._detect_current_page()
            self._home_page.click_view_all_cars()
            self._current_page = Pages.CARS
            self._cars_page = CarsPage(self._page_client)

    def ensure_on_home_page(self) -> None:
        """Ensure we're on home page (requires authentication)"""
        if self._current_page != Pages.HOME:
            self._page_client = self._client.navigate_to_base()
            self._detect_current_page()

            if self._current_page != Pages.HOME:
                raise Exception(
                    "Expected to land on home page but landed on login - not authenticated"
                )

    def _detect_current_page(self) -> None:
        self._home_page = HomePage(self._page_client)
        self._login_page = LoginPage(self._page_client)
        if self._login_page.is_current_page():
            self._current_page = Pages.LOGIN
        elif self._home_page.is_current_page():
            self._current_page = Pages.HOME
        else:
            self._current_page = Pages.NONE
