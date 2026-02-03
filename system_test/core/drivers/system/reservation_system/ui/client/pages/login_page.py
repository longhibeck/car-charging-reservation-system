from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from system_test.core.drivers.system.reservation_system.ui.client.pages.base_page import (
    BasePage,
)


class LoginPage(BasePage):
    USERNAME_LABEL = "Username"
    PASSWORD_LABEL = "Password"
    LOGIN_BUTTON_NAME = "Login"

    def __init__(self, page_client: PageTestClient):
        super().__init__(page_client)

    def is_current_page(self) -> bool:
        return self._page_client.is_label_visible(
            LoginPage.USERNAME_LABEL
        ) and self._page_client.is_label_visible(LoginPage.PASSWORD_LABEL)

    def input_username(self, value: str):
        self._page_client.fill_input_by_label(self.USERNAME_LABEL, value)

    def input_password(self, value: str):
        self._page_client.fill_input_by_label(self.PASSWORD_LABEL, value)

    def click_login(self):
        self._page_client.click_button(name=self.LOGIN_BUTTON_NAME)
