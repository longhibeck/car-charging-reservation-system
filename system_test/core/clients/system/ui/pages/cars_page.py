from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import expect
from system_test.core.clients.commons.page_test_client import PageTestClient

if TYPE_CHECKING:
    from system_test.core.clients.system.ui.pages.add_car_page import AddCarPage


class CarsPage:
    """Page Object for Cars List Page"""

    # Selectors
    PAGE_TITLE = "Your Cars"
    VIEW_ALL_BUTTON = "View All"
    ADD_CAR_BUTTON = "Add Car"

    def __init__(self, page_client: PageTestClient):
        self.page_client = page_client

    # Query methods
    def is_loaded(self) -> bool:
        """Check if cars page is loaded"""
        return self.page_client.is_visible_by_role("heading", name=self.PAGE_TITLE)

    # Assertion methods
    def assert_loaded(self):
        """Assert cars page is loaded"""
        expect(
            self.page_client.page.get_by_role("heading", name=self.PAGE_TITLE)
        ).to_be_visible()

    def assert_car_in_table(
        self, car_name: str, battery_size: str, max_kw_ac: str, max_kw_dc: str
    ):
        """Assert car appears in table with correct values"""
        expect(self.page_client.page.get_by_role("cell", name=car_name)).to_be_visible()
        expect(
            self.page_client.page.get_by_role("cell", name=battery_size)
        ).to_be_visible()
        expect(
            self.page_client.page.get_by_role("cell", name=max_kw_ac)
        ).to_be_visible()
        expect(
            self.page_client.page.get_by_role("cell", name=max_kw_dc)
        ).to_be_visible()

    # Action methods
    def click_view_all(self):
        """Click View All button to see all cars"""
        self.page_client.click_by_role("button", name=self.VIEW_ALL_BUTTON)
        # Wait for page to load
        self.page_client.page.wait_for_load_state("networkidle")
        return self  # Return self since we stay on cars page

    def click_add_car(self) -> AddCarPage:
        """Navigate to add car page"""
        from system_test.core.clients.system.ui.pages.add_car_page import AddCarPage
        
        self.page_client.click_by_role("button", name=self.ADD_CAR_BUTTON, exact=True)
        return AddCarPage(self.page_client)
