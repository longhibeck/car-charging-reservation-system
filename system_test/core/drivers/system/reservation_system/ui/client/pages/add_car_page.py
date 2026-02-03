from __future__ import annotations

from typing import TYPE_CHECKING

from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from system_test.core.drivers.system.reservation_system.ui.client.pages.base_page import (
    BasePage,
)

if TYPE_CHECKING:
    from system_test.core.drivers.system.reservation_system.ui.client.pages.cars_page import (
        CarsPage,
    )


class AddCarPage(BasePage):
    # Form field IDs
    CAR_NAME_LOCATOR = "#car-name"
    BATTERY_CHARGE_LIMIT_LOCATOR = "#battery-charge-limit"
    BATTERY_SIZE_LOCATOR = "#battery-size"
    MAX_KW_AC_LOCATOR = "#max-kw-ac"
    MAX_KW_DC_LOCATOR = "#max-kw-dc"
    # Connector types
    CONNECTOR_TYPE_2_LOCATOR = "#connector-TYPE_2"
    CONNECTOR_CCS_LOCATOR = "#connector-CCS"
    CONNECTOR_CHADEMO_LOCATOR = "#connector-CHADEMO"
    CONNECTOR_SCHUKO_LOCATOR = "#connector-SCHUKO"
    # Buttons
    ADD_CAR_BUTTON_NAME = "Add Car"
    PAGE_TITLE = "Add Car"

    def __init__(self, page_client: PageTestClient):
        super().__init__(page_client)

    def input_car_name(self, value: str) -> None:
        self._page_client.fill(self.CAR_NAME_LOCATOR, value)

    def input_battery_charge_limit(self, value: str) -> None:
        self._page_client.fill(self.BATTERY_CHARGE_LIMIT_LOCATOR, value)

    def input_battery_size(self, value: str) -> None:
        self._page_client.fill(self.BATTERY_SIZE_LOCATOR, value)

    def input_max_kw_ac(self, value: str) -> None:
        self._page_client.fill(self.MAX_KW_AC_LOCATOR, value)

    def input_max_kw_dc(self, value: str) -> None:
        self._page_client.fill(self.MAX_KW_DC_LOCATOR, value)

    def check_connector_type_2(self) -> None:
        self._page_client.check_checkbox(self.CONNECTOR_TYPE_2_LOCATOR)

    def check_connector_ccs(self) -> None:
        self._page_client.check_checkbox(self.CONNECTOR_CCS_LOCATOR)

    def check_connector_chademo(self) -> None:
        self._page_client.check_checkbox(self.CONNECTOR_CHADEMO_LOCATOR)

    def check_connector_schuko(self) -> None:
        self._page_client.check_checkbox(self.CONNECTOR_SCHUKO_LOCATOR)

    def click_add_car(self) -> CarsPage:
        from system_test.core.drivers.system.reservation_system.ui.client.pages.cars_page import (
        CarsPage,
    )
        self._page_client.click_button(name=self.ADD_CAR_BUTTON_NAME)
        return CarsPage(self._page_client)
