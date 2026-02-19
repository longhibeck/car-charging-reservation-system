

from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from system_test.core.drivers.system.reservation_system.ui.client.pages.base_page import (
    BasePage,
)
from system_test.core.drivers.system.reservation_system.ui.client.pages.cars_page import CarsPage
from system_test.core.drivers.system.reservation_system.ui.client.pages.login_page  import LoginPage


class HomePage(BasePage):
    VIEW_CARS_BUTTON_NAME = "View All"
    LOGIN_BUTTON_NAME = "Login"
    YOUR_RESERVATIONS_HEADING = "Your Reservations"
    YOUR_CARS_HEADING = "Your Cars"

    def __init__(self, page_client: PageTestClient):
        super().__init__(page_client)

    def is_current_page(self) -> bool:
        return self._page_client.is_heading_visible(HomePage.YOUR_RESERVATIONS_HEADING) and \
               self._page_client.is_heading_visible(HomePage.YOUR_CARS_HEADING)

    def click_login(self) -> LoginPage:
        self._page_client.click_button(self.LOGIN_BUTTON_NAME)
        return LoginPage(self._page_client)

    def click_view_all_cars(self) -> CarsPage:
        self._page_client.click_button(self.VIEW_CARS_BUTTON_NAME)
        return CarsPage(self._page_client)
