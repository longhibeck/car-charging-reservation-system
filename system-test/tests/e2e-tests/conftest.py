import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def logged_in_page(page):
    page.goto("http://localhost:8080/")
    page.get_by_label("Username").fill("addisonw")
    page.get_by_label("Password").fill("addisonwpass")
    page.get_by_role("button", name="Login").click()
    return page
