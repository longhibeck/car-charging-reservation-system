from playwright.sync_api import Page, Response
from system_test.core.clients.commons.page_test_client import PageTestClient
from system_test.core.clients.system.ui.pages.home_page import HomePage
from system_test.core.clients.system.ui.pages.login_page import LoginPage


class CarChargingReservationUiClient:
    """UI Client for Car Charging Reservation System using Playwright"""

    # Constants
    CONTENT_TYPE = "content-type"
    TEXT_HTML = "text/html"

    def __init__(self, page: Page, base_url: str):
        self._page = page
        self.base_url = base_url
        self._page_client = PageTestClient(page, base_url)
        self._response: Response | None = None

    @staticmethod
    def create(page: Page, base_url: str) -> "CarChargingReservationUiClient":
        """Factory method to create client"""
        return CarChargingReservationUiClient(page, base_url)

    def is_authenticated(self) -> bool:
        """
        Check if user is authenticated by examining auth state.
        Tries multiple strategies to detect authentication.
        """
        # Create page objects on-demand for checking
        home_page = HomePage(self._page_client)
        login_page = LoginPage(self._page_client)
        
        # Primary strategy: Check if we're seeing authenticated UI
        if home_page.is_loaded():
            return True
        
        # Fallback: Check if we're on login page (proves NOT authenticated)
        if login_page.is_loaded():
            return False

        # Strategy 1: Check for auth token in localStorage
        token = self._page.evaluate("() => localStorage.getItem('token')")
        if token:
            return True

        # Strategy 2: Check for auth token in sessionStorage
        session_token = self._page.evaluate("() => sessionStorage.getItem('token')")
        if session_token:
            return True
        
        # Strategy 3: Check for auth token in cookies
        cookies = self._page.context.cookies()
        auth_cookie = next((c for c in cookies if c['name'] in ['auth_token', 'access_token', 'jwt']), None)
        if auth_cookie:
            return True
        
        return False

    def navigate_to_home(self) -> HomePage | LoginPage:
        """
        Navigate to home page URL.
        For SPAs, checks authentication state after client-side routing.
        Returns LoginPage if not authenticated, HomePage if authenticated.
        """
        self._response = self._page.goto(self.base_url)

        if not self._response:
            raise Exception("No response from navigation")

        # Wait for SPA to finish client-side routing
        self._page.wait_for_load_state("networkidle")

        # Create page objects on-demand and return the appropriate one
        if self.is_authenticated():
            return HomePage(self._page_client)
        else:
            return LoginPage(self._page_client)

    def open_home_page(self) -> HomePage:
        """
        Open home page (requires authentication).
        Use this after logging in when you expect to see the home page.
        """
        self._response = self._page.goto(self.base_url)
        if not self._response:
            raise Exception("No response from navigation")
        
        self._page.wait_for_load_state("networkidle")
        return HomePage(self._page_client)
    
    def assert_home_page_loaded(self) -> None:
        """
        Assert that the home page loaded successfully.
        Checks HTTP status, content type, and page initialization.
        """
        if not self._response:
            raise AssertionError("No response available")
        
        # Check HTTP status
        if self._response.status != 200:
            raise AssertionError(f"Expected status 200 but got {self._response.status}")
        
        # Check Content-Type header
        content_type = self._response.headers.get(self.CONTENT_TYPE, "")
        if not content_type or self.TEXT_HTML not in content_type:
            raise AssertionError(f"Content-Type should be text/html, but was: {content_type}")
        
        # Check page is initialized
        if not self._page:
            raise AssertionError("Page is not initialized")
        
        # Create home page on-demand to check if loaded
        home_page = HomePage(self._page_client)
        if not home_page.is_loaded():
            raise AssertionError("Home page HTML loaded but UI elements not visible")
    
    def assert_response_ok(self) -> None:
        """Assert last response was successful (200 OK)"""
        if not self._response:
            raise AssertionError("No response available")
        
        if self._response.status != 200:
            raise AssertionError(f"Expected status 200 but got {self._response.status}")
    
    def assert_response_is_html(self) -> None:
        """Assert last response content type is HTML"""
        if not self._response:
            raise AssertionError("No response available")
        
        content_type = self._response.headers.get(self.CONTENT_TYPE, "")
        if not content_type or self.TEXT_HTML not in content_type:
            raise AssertionError(f"Expected Content-Type to contain '{self.TEXT_HTML}', but was: {content_type}")
    
    def get_response_status(self) -> int | None:
        """Get status code of last response"""
        return self._response.status if self._response else None
    
    def get_response_content_type(self) -> str | None:
        """Get content type of last response"""
        if not self._response:
            return None
        return self._response.headers.get(self.CONTENT_TYPE)

    @property
    def page(self) -> Page:
        """Get underlying Playwright page"""
        return self._page
    
    @property
    def page_client(self) -> PageTestClient:
        """Get page client for creating page objects"""
        return self._page_client