from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import expect
from system_test.core.clients.commons.page_test_client import PageTestClient

if TYPE_CHECKING:
    from system_test.core.clients.system.ui.pages.cars_page import CarsPage


class AddCarPage:
    """Page Object for Add Car Page"""

    # Form field IDs
    CAR_NAME_ID = "car-name"
    BATTERY_CHARGE_LIMIT_ID = "battery-charge-limit"
    BATTERY_SIZE_ID = "battery-size"
    MAX_KW_AC_ID = "max-kw-ac"
    MAX_KW_DC_ID = "max-kw-dc"

    # Connector types
    CONNECTOR_TYPE_2_ID = "connector-TYPE_2"
    CONNECTOR_CCS_ID = "connector-CCS"
    CONNECTOR_CHADEMO_ID = "connector-CHADEMO"
    CONNECTOR_SCHUKO_ID = "connector-SCHUKO"

    # Buttons
    ADD_CAR_BUTTON = "Add Car"
    PAGE_TITLE = "Add Car"

    def __init__(self, page_client: PageTestClient):
        self.page_client = page_client

    # Query methods
    def is_loaded(self) -> bool:
        """Check if add car page is loaded"""
        return self.page_client.is_visible_by_role("heading", name=self.PAGE_TITLE)

    def get_car_name_validation_message(self) -> str:
        """Get validation message for car name field"""
        return self.page_client.page.locator(f"#{self.CAR_NAME_ID}").evaluate(
            "el => el.validationMessage"
        )

    # Assertion methods
    def assert_loaded(self):
        """Assert add car page is loaded"""
        expect(
            self.page_client.page.get_by_role("heading", name=self.PAGE_TITLE)
        ).to_be_visible()

    # Form interaction methods
    def fill_car_name(self, name: str):
        """Fill car name field"""
        self.page_client.page.locator(f"#{self.CAR_NAME_ID}").fill(name)

    def fill_battery_charge_limit(self, limit: str):
        """Fill battery charge limit field"""
        self.page_client.page.locator(f"#{self.BATTERY_CHARGE_LIMIT_ID}").fill(limit)

    def fill_battery_size(self, size: str):
        """Fill battery size field"""
        self.page_client.page.locator(f"#{self.BATTERY_SIZE_ID}").fill(size)

    def fill_max_kw_ac(self, kw: str):
        """Fill max kW AC field"""
        self.page_client.page.locator(f"#{self.MAX_KW_AC_ID}").fill(kw)

    def fill_max_kw_dc(self, kw: str):
        """Fill max kW DC field"""
        self.page_client.page.locator(f"#{self.MAX_KW_DC_ID}").fill(kw)

    def select_connector_type_2(self):
        """Select TYPE_2 connector"""
        self.page_client.page.locator(f"#{self.CONNECTOR_TYPE_2_ID}").check()

    def select_connector_ccs(self):
        """Select CCS connector"""
        self.page_client.page.locator(f"#{self.CONNECTOR_CCS_ID}").check()

    def select_connector_chademo(self):
        """Select CHAdeMO connector"""
        self.page_client.page.locator(f"#{self.CONNECTOR_CHADEMO_ID}").check()

    def select_connector_schuko(self):
        """Select Schuko connector"""
        self.page_client.page.locator(f"#{self.CONNECTOR_SCHUKO_ID}").check()

    def click_add_car(self) -> CarsPage:
        """Click Add Car button to submit form"""
        from system_test.core.clients.system.ui.pages.cars_page import CarsPage
        
        self.page_client.click_by_role("button", name=self.ADD_CAR_BUTTON, exact=True)
        
        # Wait for navigation or error
        self.page_client.page.wait_for_load_state("networkidle")
        
        # Return CarsPage since we navigate back after successful add
        return CarsPage(self.page_client)

    # Composite action methods
    def add_car(
        self,
        name: str,
        battery_charge_limit: str,
        battery_size: str,
        max_kw_ac: str,
        max_kw_dc: str,
        connector_type_2: bool = False,
        connector_ccs: bool = False,
        connector_chademo: bool = False,
        connector_schuko: bool = False,
    ):
        """
        Fill out complete add car form and submit.
        Returns CarsPage after successful submission.
        """
        if name:
            self.fill_car_name(name)

        if connector_type_2:
            self.select_connector_type_2()
        if connector_ccs:
            self.select_connector_ccs()
        if connector_chademo:
            self.select_connector_chademo()
        if connector_schuko:
            self.select_connector_chademo()

        self.fill_battery_charge_limit(battery_charge_limit)
        self.fill_battery_size(battery_size)
        self.fill_max_kw_ac(max_kw_ac)
        self.fill_max_kw_dc(max_kw_dc)

        return self.click_add_car()
