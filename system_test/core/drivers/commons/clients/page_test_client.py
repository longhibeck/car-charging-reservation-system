from playwright.sync_api import Page


class PageTestClient:
    DEFAULT_TIMEOUT_SECONDS = 10
    DEFAULT_TIMEOUT_MILLISECONDS = DEFAULT_TIMEOUT_SECONDS * 1000

    def __init__(
        self,
        page: Page,
        base_url: str,
        timeout_milliseconds: int = DEFAULT_TIMEOUT_MILLISECONDS,
    ):
        self._page = page
        self._base_url = base_url
        self._timeout_milliseconds = timeout_milliseconds

    def get_base_url(self) -> str:
        return self._base_url

    def get_page(self) -> Page:
        return self._page

    def fill(self, selector: str, value: str) -> None:
        self._page.fill(selector, value)

    def click(self, selector: str) -> None:
        self._page.click(selector)

    def click_button(self, name: str) -> None:
        self._page.get_by_role("button", name=name, exact=True).click()

    def fill_input_by_label(self, label: str, value: str) -> None:
        self._page.get_by_label(label).fill(value)

    def check_checkbox(self, selector: str) -> None:
        self._page.check(selector)

    def is_label_visible(self, label: str) -> bool:
        try:
            return self._page.get_by_label(label).is_visible(
                timeout=self._timeout_milliseconds
            )
        except Exception:
            return False

    def is_heading_visible(self, name: str) -> bool:
        try:
            return self._page.get_by_role("heading", name=name).is_visible(
                timeout=self._timeout_milliseconds
            )
        except Exception:
            return False

    def get_element_text(self, selector: str) -> str | None:
        """Get text content from an element by selector"""
        try:
            element = self._page.locator(selector)
            if element.is_visible(timeout=self._timeout_milliseconds):
                return element.text_content()
            return None
        except Exception:
            return None

    def is_element_visible(self, selector: str) -> bool:
        """Check if an element is visible by selector"""
        try:
            return self._page.locator(selector).is_visible(
                timeout=self._timeout_milliseconds
            )
        except Exception:
            return False

    def get_validation_message(self, selector: str) -> str:
        """Get HTML5 validation message from an input element"""
        return self._page.locator(selector).evaluate("el => el.validationMessage")

    def goto(self, path: str = "/"):
        """Navigate to a path relative to base_url"""
        url = f"{self.base_url}{path}"
        return self.page.goto(url)
