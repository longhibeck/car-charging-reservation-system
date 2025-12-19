from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import expect
from system_test.core.clients.commons.page_test_client import PageTestClient

if TYPE_CHECKING:
    from system_test.core.clients.system.ui.pages.cars_page import CarsPage


class HomePage:
    """Page Object for Home Page (requires authentication)"""

    # Selectors for authenticated home page
    YOUR_RESERVATIONS_HEADING = "Your Reservations"
    YOUR_CARS_HEADING = "Your Cars"
    NEW_RESERVATION_BUTTON = "New Reservation"
    RESERVATION_HISTORY_BUTTON = "Reservation History"

    def __init__(self, page_client: PageTestClient):
        self.page_client = page_client

    # Query methods (no assertions) - for flexibility in tests
    def is_loaded(self) -> bool:
        """Check if home page is loaded (user is authenticated)"""
        return self.page_client.is_visible_by_role(
            "heading", name=self.YOUR_RESERVATIONS_HEADING
        ) and self.page_client.is_visible_by_role(
            "heading", name=self.YOUR_CARS_HEADING
        )

    def has_your_reservations_heading(self) -> bool:
        """Check if 'Your Reservations' heading is visible"""
        return self.page_client.is_visible_by_role(
            "heading", name=self.YOUR_RESERVATIONS_HEADING
        )

    def has_your_cars_heading(self) -> bool:
        """Check if 'Your Cars' heading is visible"""
        return self.page_client.is_visible_by_role(
            "heading", name=self.YOUR_CARS_HEADING
        )

    def has_new_reservation_button(self) -> bool:
        """Check if 'New Reservation' button is visible"""
        return self.page_client.is_visible_by_role(
            "button", name=self.NEW_RESERVATION_BUTTON
        )

    def has_reservation_history_button(self) -> bool:
        """Check if 'Reservation History' button is visible"""
        return self.page_client.is_visible_by_role(
            "button", name=self.RESERVATION_HISTORY_BUTTON
        )

    # Assertion methods - for convenience (commonly used assertions)
    def assert_loaded(self):
        """Assert home page is loaded with all expected elements"""
        expect(
            self.page_client.page.get_by_role(
                "heading", name=self.YOUR_RESERVATIONS_HEADING
            )
        ).to_be_visible()
        expect(
            self.page_client.page.get_by_role("heading", name=self.YOUR_CARS_HEADING)
        ).to_be_visible()

    def assert_your_reservations_heading_visible(self):
        """Assert 'Your Reservations' heading is visible"""
        expect(
            self.page_client.page.get_by_role(
                "heading", name=self.YOUR_RESERVATIONS_HEADING
            )
        ).to_be_visible()

    def assert_your_cars_heading_visible(self):
        """Assert 'Your Cars' heading is visible"""
        expect(
            self.page_client.page.get_by_role("heading", name=self.YOUR_CARS_HEADING)
        ).to_be_visible()

    def click_view_all_cars(self) -> CarsPage:
        """Navigate to all cars page"""
        from system_test.core.clients.system.ui.pages.cars_page import CarsPage
        
        self.page_client.click_by_role("button", name="View All")
        return CarsPage(self.page_client)
