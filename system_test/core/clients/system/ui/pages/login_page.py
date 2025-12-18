from playwright.sync_api import expect
from system_test.core.clients.commons.page_test_client import PageTestClient

from system_test.core.clients.system.ui.pages.home_page import HomePage


class LoginPage:
    """Page Object for Login Page"""

    # Labels and text
    LOGIN_HEADING = "Login"
    USERNAME_LABEL = "Username"
    PASSWORD_LABEL = "Password"
    LOGIN_BUTTON = "Login"
    LOGIN_FAILED_TEXT = "Login failed"

    def __init__(self, page_client: PageTestClient):
        self.page_client = page_client

    def is_loaded(self) -> bool:
        """Check if login page is loaded"""
        return self.page_client.is_visible_by_label(
            self.USERNAME_LABEL
        ) and self.page_client.is_visible_by_label(self.PASSWORD_LABEL)

    def assert_loaded(self):
        """Assert login page is loaded with all expected elements"""
        expect(
            self.page_client.page.get_by_role("heading", name=self.LOGIN_HEADING)
        ).to_be_visible()

    def fill_username(self, username: str):
        """Fill username field"""
        self.page_client.fill_by_label(self.USERNAME_LABEL, username)

    def fill_password(self, password: str):
        """Fill password field"""
        self.page_client.fill_by_label(self.PASSWORD_LABEL, password)

    def click_login(self):
        """Click login button (doesn't wait for navigation)"""
        self.page_client.click_by_role("button", name=self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Complete login flow and return HomePage after successful login"""

        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

        # After successful login, we're on home page
        return HomePage(self.page_client)

    def assert_login_successful(self):
        """Assert login was successful by checking we're on home page"""
        expect(
            self.page_client.page.get_by_role("heading", name="Your Reservations")
        ).to_be_visible()

    def assert_login_failed(self):
        """Assert login failed message is visible"""
        expect(
            self.page_client.page.get_by_text(self.LOGIN_FAILED_TEXT)
        ).to_be_visible()

    def get_password_validation_message(self) -> str:
        """Get HTML5 validation message from password field"""
        return self.page_client.get_validation_message_by_label(self.PASSWORD_LABEL)

    def assert_password_validation_message(self, expected_message: str):
        """Assert password field validation message matches expected"""
        actual_message = self.get_password_validation_message()
        assert actual_message == expected_message, (
            f"Expected validation message '{expected_message}', but got '{actual_message}'"
        )
