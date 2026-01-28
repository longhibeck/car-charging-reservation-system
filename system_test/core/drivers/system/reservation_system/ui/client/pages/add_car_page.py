
from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from system_test.core.drivers.system.reservation_system.ui.client.pages.cars_page import CarsPage



class AddCarPage:
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
        self.page_client = page_client

    def input_car_name(self, name: str):
        self.page_client.fill(self.CAR_NAME_LOCATOR, name)

    def input_battery_charge_limit(self, value: str):
        self.page_client.fill(self.BATTERY_CHARGE_LIMIT_LOCATOR, value)

    def input_battery_size(self, value: str):
        self.page_client.fill(self.BATTERY_SIZE_LOCATOR, value)

    def input_max_kw_ac(self, value: str):
        self.page_client.fill(self.MAX_KW_AC_LOCATOR, value)

    def input_max_kw_dc(self, value: str):
        self.page_client.fill(self.MAX_KW_DC_LOCATOR, value)

    def check_connector_type_2(self):
        self.page_client.check_checkbox(self.CONNECTOR_TYPE_2_LOCATOR)

    def check_connector_ccs(self):
        self.page_client.check_checkbox(self.CONNECTOR_CCS_LOCATOR)

    def check_connector_chademo(self):
        self.page_client.check_checkbox(self.CONNECTOR_CHADEMO_LOCATOR)

    def check_connector_schuko(self):
        self.page_client.check_checkbox(self.CONNECTOR_SCHUKO_LOCATOR)

    def click_add_car(self) -> CarsPage:
        from system_test.core.clients.system.ui.pages.cars_page import CarsPage

        self.page_client.click_button(name=self.ADD_CAR_BUTTON_NAME)
        #  self.page_client.page.wait_for_load_state("networkidle")
        return CarsPage(self.page_client)

    ####################################################

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
