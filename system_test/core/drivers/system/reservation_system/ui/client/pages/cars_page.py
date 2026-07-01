from __future__ import annotations

from typing import TYPE_CHECKING

from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from system_test.core.drivers.system.reservation_system.ui.client.pages.base_page import (
    BasePage,
)

if TYPE_CHECKING:
    from system_test.core.drivers.system.reservation_system.ui.client.pages.add_car_page import (
        AddCarPage,
    )


class CarsPage(BasePage):
    PAGE_TITLE = "Your Cars"
    VIEW_ALL_BUTTON_NAME = "View All"
    ADD_CAR_BUTTON_NAME = "Add Car"

    _LAST_ROW = "#cars-table-body tr:last-child"
    _NAME_CELL = "[data-testid='car-name']"
    _CONNECTORS_CELL = "[data-testid='car-connectors']"
    _BATTERY_LIMIT_CELL = "[data-testid='car-battery-limit']"
    _BATTERY_SIZE_CELL = "[data-testid='car-battery-size']"
    _MAX_KW_AC_CELL = "[data-testid='car-max-kw-ac']"
    _MAX_KW_DC_CELL = "[data-testid='car-max-kw-dc']"

    def __init__(self, page_client: PageTestClient):
        super().__init__(page_client)

    def click_view_all(self) -> None:
        self._page_client.click_button(self.VIEW_ALL_BUTTON_NAME)

    def click_add_car(self) -> AddCarPage:
        from system_test.core.drivers.system.reservation_system.ui.client.pages.add_car_page import (
            AddCarPage,
        )

        self._page_client.click_button(self.ADD_CAR_BUTTON_NAME)
        return AddCarPage(self._page_client)

    def read_last_car(self) -> dict:
        """Read the last row of the cars table — the car most recently added."""

        def _int(selector: str) -> int:
            return int(self._page_client.read_text_content(selector) or "0")

        row = self._page_client.get_page().locator(self._LAST_ROW)
        car_id = row.get_attribute("data-car-id") or ""
        connectors_text = self._page_client.read_text_content(
            f"{self._LAST_ROW} {self._CONNECTORS_CELL}"
        )
        connector_types = [
            c.strip()
            for c in connectors_text.split(",")
            if c.strip() and c.strip() != "-"
        ]

        return {
            "id": car_id,
            "name": self._page_client.read_text_content(
                f"{self._LAST_ROW} {self._NAME_CELL}"
            ),
            "connector_types": connector_types,
            "battery_charge_limit": _int(
                f"{self._LAST_ROW} {self._BATTERY_LIMIT_CELL}"
            ),
            "battery_size": _int(f"{self._LAST_ROW} {self._BATTERY_SIZE_CELL}"),
            "max_kw_ac": _int(f"{self._LAST_ROW} {self._MAX_KW_AC_CELL}"),
            "max_kw_dc": _int(f"{self._LAST_ROW} {self._MAX_KW_DC_CELL}"),
        }

    def read_all_cars(self) -> list[dict]:
        """Read every row of the cars table."""
        rows = self._page_client.get_page().locator("#cars-table-body tr").all()
        result = []
        for row in rows:

            def _cell(testid: str) -> str:
                return row.locator(f"[data-testid='{testid}']").text_content() or ""

            connectors_text = _cell("car-connectors")
            connector_types = [
                c.strip()
                for c in connectors_text.split(",")
                if c.strip() and c.strip() != "-"
            ]
            result.append(
                {
                    "id": row.get_attribute("data-car-id") or "",
                    "name": _cell("car-name"),
                    "connector_types": connector_types,
                    "battery_charge_limit": int(_cell("car-battery-limit") or "0"),
                    "battery_size": int(_cell("car-battery-size") or "0"),
                    "max_kw_ac": int(_cell("car-max-kw-ac") or "0"),
                    "max_kw_dc": int(_cell("car-max-kw-dc") or "0"),
                }
            )
        return result
