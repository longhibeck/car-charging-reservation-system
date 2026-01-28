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

    @staticmethod
    def is_current_page(page_client: PageTestClient) -> bool:
        return page_client.is_label_visible(LoginPage.USERNAME_LABEL) and \
               page_client.is_label_visible(LoginPage.PASSWORD_LABEL)

    def input_username(self, value: str):
        self._page_client.fill_input_by_label(self.USERNAME_LABEL, value)

    def input_password(self, value: str):
        self._page_client.fill_input_by_label(self.PASSWORD_LABEL, value)

    def click_login(self):
        self._page_client.click_button(name=self.LOGIN_BUTTON_NAME)

    # def login(self, username: str, password: str) -> HomePage:
    #     from system_test.core.clients.system.ui.pages.home_page import HomePage

    #     self.input_username(username)
    #     self.input_password(password)
    #     self.click_login()

    #     return HomePage(self.page_client)
