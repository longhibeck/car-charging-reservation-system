from playwright.sync_api import Page


class PageTestClient:
    """Wrapper for Playwright Page with test utilities"""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def goto(self, path: str = "/"):
        """Navigate to a path relative to base_url"""
        url = f"{self.base_url}{path}"
        return self.page.goto(url)

    def click(self, selector: str):
        """Click an element"""
        self.page.click(selector)

    def click_by_role(self, role: str, name: str, exact: bool = False):
        """Click element by role and name"""
        self.page.get_by_role(role, name=name, exact=exact).click()

    def fill(self, selector: str, value: str):
        """Fill an input field"""
        self.page.fill(selector, value)

    def fill_by_label(self, label: str, value: str):
        """Fill input field by label"""
        self.page.get_by_label(label).fill(value)

    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.locator(selector).text_content() or ""

    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(selector).is_visible()

    def is_visible_by_label(self, label: str) -> bool:
        """Check if element by role and name is visible"""
        try:
            return self.page.get_by_label(label).is_visible()
        except Exception:
            return False

    def is_visible_by_role(self, role: str, name: str) -> bool:
        """Check if element by role and name is visible"""
        try:
            return self.page.get_by_role(role, name=name).is_visible()
        except Exception:
            return False

    def wait_for_selector(self, selector: str, timeout: int = 30000):
        """Wait for element to appear"""
        self.page.wait_for_selector(selector, timeout=timeout)

    def get_validation_message_by_label(self, label: str) -> str:
        """Get HTML5 validation message from an input field by label"""
        return self.page.get_by_label(label).evaluate(
            "element => element.validationMessage"
        )
