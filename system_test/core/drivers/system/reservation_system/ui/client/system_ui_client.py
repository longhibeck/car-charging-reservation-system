from system_test.core.drivers.system.reservation_system.ui.client.pages.home_page import (
    HomePage,
)
from playwright.sync_api import Page, Response
from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from http import HTTPStatus


class SystemUiClient:
    CONTENT_TYPE = "content-type"
    TEXT_HTML = "text/html"
    HTML_OPENING_TAG = "<html"
    HTML_CLOSING_TAG = "</html>"

    def __init__(self, page: Page, base_url: str) -> None:
        self._page = page
        self._base_url = base_url
        self._home_page = None  # as HomePage
        self._response: Response | None = None

    def navigate_to_base(self) -> PageTestClient:
        self._response = self._page.goto(self._base_url)
        return PageTestClient(self._page, self._base_url)

    def is_status_ok(self) -> bool:
        return self._response.status == HTTPStatus.OK

    def is_page_loaded(self) -> bool:
        if not self._response or not self.is_status_ok() or not self._page:
            return False

        content_type = self._response.headers.get(self.CONTENT_TYPE, "")

        if not content_type or content_type != self.TEXT_HTML:
            return False

        page_content = self._page.content().lower()
        if (
            not page_content
            or self.HTML_OPENING_TAG not in page_content
            or self.HTML_CLOSING_TAG not in page_content
        ):
            return False
        
        return True
