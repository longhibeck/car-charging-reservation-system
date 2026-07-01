from enum import StrEnum
from typing import Optional

from system_test.core.drivers.commons.clients.closer import Closer
from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from system_test.core.drivers.commons.result import Result
from system_test.core.drivers.system.commons.dtos.auth_response import LoginResponse
from system_test.core.drivers.system.commons.dtos.car_request import AddCarRequest
from system_test.core.drivers.system.commons.dtos.car_response import (
    AddCarResponse,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.add_car_page import (
    AddCarPage,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.cars_page import (
    CarsPage,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.home_page import (
    HomePage,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.login_page import (
    LoginPage,
)
from system_test.core.drivers.system.reservation_system.ui.client.system_ui_client import (
    SystemUiClient,
)
from system_test.core.drivers.system.system_driver import SystemDriver


class Pages(StrEnum):
    NONE = "none"
    CARS = "cars"
    ADD_CAR = "add_car"
    HOME = "home"
    LOGIN = "login"


class SystemUiDriver(SystemDriver):
    def __init__(self, base_url: str) -> None:
        self._client = SystemUiClient(base_url)
        self._page_client: Optional[PageTestClient] = None
        self._current_page: Pages = Pages.NONE
        self._home_page: Optional[HomePage] = None
        self._login_page: Optional[LoginPage] = None
        self._cars_page: Optional[CarsPage] = None
        self._add_car_page: Optional[AddCarPage] = None

    def go_to_system(self) -> Result[None]:
        self._page_client = self._client.navigate_to_base()

        if not self._client.is_status_ok() or not self._client.is_page_loaded():
            return Result.failure("Failed to load system page")

        self._detect_current_page()
        return Result.success()

    def login(self, request) -> Result[LoginResponse]:
        self.ensure_on_login_page()
        assert self._login_page is not None
        self._login_page.input_username(request["username"])
        self._login_page.input_password(request["password"])
        self._login_page.click_login()

        # Wait for navigation or error message to appear
        assert self._page_client is not None
        self._page_client.get_page().wait_for_load_state("networkidle")

        # Small additional wait to ensure error messages are rendered
        self._page_client.get_page().wait_for_timeout(500)

        self._detect_current_page()

        if self._current_page != Pages.HOME:
            assert self._login_page is not None
            error_message = self._login_page.get_error_message()
            if error_message:
                return Result.failure(error_message)
            return Result.failure("Login failed - still on login page")

        # Return a stub LoginResponse for UI testing
        return Result.success(
            {
                "access_token": "ui-token",
                "refresh_token": "ui-refresh",
                "token_type": "Bearer",
                "user": {
                    "id": 0,
                    "username": request.get("username", ""),
                    "external_user_id": 0,
                },
            }
        )

    def add_car(self, request: AddCarRequest) -> Result[AddCarResponse]:
        self.ensure_on_cars_page()
        assert self._cars_page is not None
        self._add_car_page = self._cars_page.click_add_car()
        assert self._add_car_page is not None

        self._add_car_page.input_car_name(request["name"])
        self._add_car_page.input_battery_charge_limit(
            str(request["battery_charge_limit"])
        )
        self._add_car_page.input_battery_size(str(request["battery_size"]))
        self._add_car_page.input_max_kw_ac(str(request["max_kw_ac"]))
        self._add_car_page.input_max_kw_dc(str(request["max_kw_dc"]))

        for connector_type in request["connector_types"]:
            if connector_type == "Type 2":
                self._add_car_page.check_connector_type_2()
            elif connector_type == "CCS":
                self._add_car_page.check_connector_ccs()
            elif connector_type == "CHAdeMO":
                self._add_car_page.check_connector_chademo()
            elif connector_type == "Schuko":
                self._add_car_page.check_connector_schuko()

        self._cars_page = self._add_car_page.click_add_car()

        # Wait for navigation or error message to appear
        assert self._page_client is not None
        self._page_client.get_page().wait_for_load_state("networkidle")
        self._page_client.get_page().wait_for_timeout(500)

        # Check if we're still on the Add Car page (form validation failed)
        if self._page_client.is_heading_visible(self._add_car_page.PAGE_TITLE):
            error_message = self._add_car_page.get_error_message()
            return Result.failure(
                error_message if error_message else "Failed to add car"
            )

        self._current_page = Pages.CARS
        car_data = self._cars_page.read_last_car()
        return Result.success(
            AddCarResponse(
                id=car_data["id"],
                name=car_data["name"],
                connector_types=car_data["connector_types"],
                battery_charge_limit=car_data["battery_charge_limit"],
                battery_size=car_data["battery_size"],
                max_kw_ac=car_data["max_kw_ac"],
                max_kw_dc=car_data["max_kw_dc"],
            )
        )

    def list_cars(self) -> Result[list]:
        self.ensure_on_cars_page()
        assert self._cars_page is not None
        cars = self._cars_page.read_all_cars()
        return Result.success(
            [
                AddCarResponse(
                    id=car["id"],
                    name=car["name"],
                    connector_types=car["connector_types"],
                    battery_charge_limit=car["battery_charge_limit"],
                    battery_size=car["battery_size"],
                    max_kw_ac=car["max_kw_ac"],
                    max_kw_dc=car["max_kw_dc"],
                )
                for car in cars
            ]
        )

    def ensure_on_login_page(self) -> None:
        if self._current_page != Pages.LOGIN:
            self._page_client = self._client.navigate_to_base()
            assert self._page_client is not None
            self._detect_current_page()

            if self._current_page != Pages.LOGIN:
                raise Exception("Expected to land on login page but didn't")

    def ensure_on_cars_page(self) -> None:
        """Ensure we're on cars page"""
        if self._current_page != Pages.CARS:
            self._page_client = self._client.navigate_to_base()
            assert self._page_client is not None
            self._detect_current_page()
            assert self._home_page is not None
            self._home_page.click_view_all_cars()
            self._current_page = Pages.CARS
            self._cars_page = CarsPage(self._page_client)

    def ensure_on_home_page(self) -> None:
        """Ensure we're on home page (requires authentication)"""
        if self._current_page != Pages.HOME:
            self._page_client = self._client.navigate_to_base()
            assert self._page_client is not None
            self._detect_current_page()

            if self._current_page != Pages.HOME:
                raise Exception(
                    "Expected to land on home page but landed on login - not authenticated"
                )

    def _detect_current_page(self) -> None:
        assert self._page_client is not None
        self._home_page = HomePage(self._page_client)
        self._login_page = LoginPage(self._page_client)
        if self._login_page.is_current_page():
            self._current_page = Pages.LOGIN
        elif self._home_page.is_current_page():
            self._current_page = Pages.HOME
        else:
            self._current_page = Pages.NONE

    def close(self):
        Closer.close(self._client)
