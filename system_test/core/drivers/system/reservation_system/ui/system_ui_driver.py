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
from playwright.sync_api import Page
from enum import StrEnum


class Pages(StrEnum):
    NONE = "none"
    CARS = "cars"
    ADD_CAR = "add_car"
    HOME = "home"
    LOGIN = "login"


class SystemUiDriver(SystemDriver):
    def __init__(self, page: Page, base_url: str) -> None:
        self._client = SystemUiClient(page, base_url)
        self._page_client = None  # NOT HAPPY WITH IT
        self._current_page: Pages = Pages.NONE
        self._home_page: HomePage = None
        self._login_page: LoginPage = None
        self._cars_page: CarsPage = None

    def go_to_system(self) -> Result[None]:
        self._page_client = self._client.navigate_to_base()

        if not self._client.is_status_ok() or not self._client.is_page_loaded():
            return Result.failure()

        self._detect_current_page()
        return Result.success()

    def login(self, username: str, password: str) -> Result[None]:
        self.ensure_on_login_page()
        self._login_page.input_username(username)
        self._login_page.input_password(password)
        self._login_page.click_login()
        self._current_page = Pages.HOME
        return Result.success() 

    def add_car(
        self,
        name,
        connector_types,
        battery_charge_limit,
        battery_size,
        max_kw_ac,
        max_kw_dc,
    ):
        pass

    def list_cars(self) -> Result[list]:
        self.ensure_on_cars_page()
        return Result.success([])

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



    def ensure_on_home_page(self) -> None:
        """Ensure we're on home page (requires authentication)"""
        if self._current_page != Pages.HOME:
            self._page_client = self._client.navigate_to_base()
            self._detect_current_page()
            
            if self._current_page != Pages.HOME:
                raise Exception("Expected to land on home page but landed on login - not authenticated")

    def _detect_current_page(self) -> None:
        """Driver decides which page we're on"""
        if LoginPage.is_current_page(self._page_client):
            self._login_page = LoginPage(self._page_client)
            self._current_page = Pages.LOGIN
        elif HomePage.is_current_page(self._page_client):
            self._home_page = HomePage(self._page_client)
            self._current_page = Pages.HOME