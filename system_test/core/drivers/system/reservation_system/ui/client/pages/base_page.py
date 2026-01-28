from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from abc import ABC

class BasePage(ABC):
    NOTIFICATION_SELECTOR = "div[role='alert']"
    SUCCESS_NOTIFICATION_SELECTOR = "div[role='alert'][data-notification-type='success']"
    ERROR_NOTIFICATION_SELECTOR = "div[role='alert'][data-notification-type='error']"

    def __init__(self, page_client: PageTestClient):
        self._page_client = page_client

   