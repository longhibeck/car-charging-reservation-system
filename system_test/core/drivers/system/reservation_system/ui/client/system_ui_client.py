from playwright.sync_api import Page, Response, Browser, BrowserContext, sync_playwright
from system_test.core.drivers.commons.clients.page_test_client import PageTestClient
from http import HTTPStatus
from typing import Optional


class SystemUiClient:
    CONTENT_TYPE = "content-type"
    TEXT_HTML = "text/html"
    HTML_OPENING_TAG = "<html"
    HTML_CLOSING_TAG = "</html>"
    
    _playwright_instance = None
    _browser: Optional[Browser] = None
    _context: Optional[BrowserContext] = None
    _shared_page: Optional[Page] = None

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._home_page = None  # as HomePage
        self._response: Response | None = None
        self._page = self._get_or_create_page()
    
    @classmethod
    def _get_or_create_page(cls) -> Page:
        """Create or return existing Playwright page instance."""
        if cls._shared_page is None:
            cls._playwright_instance = sync_playwright().start()
            cls._browser = cls._playwright_instance.chromium.launch(headless=True)
            cls._context = cls._browser.new_context()
            cls._shared_page = cls._context.new_page()
        return cls._shared_page

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
    
    @classmethod
    def close(cls) -> None:
        if cls._shared_page:
            cls._shared_page.close()
            cls._shared_page = None
        if cls._context:
            cls._context.close()
            cls._context = None
        if cls._browser:
            cls._browser.close()
            cls._browser = None
        if cls._playwright_instance:
            cls._playwright_instance.stop()
            cls._playwright_instance = None
