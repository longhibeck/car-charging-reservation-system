from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from abc import ABC

class BasePage(ABC):
    NOTIFICATION_SELECTOR = "div[role='alert']"
    SUCCESS_NOTIFICATION_SELECTOR = "div[role='alert'][data-notification-type='success']"
    ERROR_NOTIFICATION_SELECTOR = "div[role='alert'][data-notification-type='error']"
    ERROR_MESSAGE_SELECTOR = "#error-message"

    def __init__(self, page_client: PageTestClient):
        self._page_client = page_client

    def get_error_message(self) -> str | None:
        """Get the error message text if visible"""
        return self._page_client.get_element_text(self.ERROR_MESSAGE_SELECTOR)

    def has_error_message(self) -> bool:
        """Check if error message is visible"""
        return self._page_client.is_element_visible(self.ERROR_MESSAGE_SELECTOR)

    def get_validation_message(self, selector: str) -> str:
        """Get HTML5 validation message from an input field (e.g., 'Please fill out this field.')"""
        return self._page_client.get_validation_message(selector)

   