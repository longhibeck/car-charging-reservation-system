from __future__ import annotations

from typing import TYPE_CHECKING

from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from system_test.core.drivers.system.reservation_system.ui.client.pages.base_page import (
    BasePage,
)

if TYPE_CHECKING:
    from system_test.core.drivers.system.reservation_system.ui.client.pages.add_car_page import AddCarPage


class CarsPage(BasePage):
    PAGE_TITLE = "Your Cars"
    VIEW_ALL_BUTTON_NAME = "View All"
    ADD_CAR_BUTTON_NAME = "Add Car"

    def __init__(self, page_client: PageTestClient):
        super().__init__(page_client)

    def click_view_all(self) -> None:
        self._page_client.click_button(self.VIEW_ALL_BUTTON_NAME)

    def click_add_car(self) -> AddCarPage:
        from system_test.core.drivers.system.reservation_system.ui.client.pages.add_car_page import AddCarPage
        self._page_client.click_button(self.ADD_CAR_BUTTON_NAME)
        return AddCarPage(self._page_client)
