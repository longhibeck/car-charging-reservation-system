from playwright.sync_api import expect


def test_dashboard_greeting(logged_in_page):
    page = logged_in_page
    expect(page.get_by_text("Welcome, addisonw")).to_be_visible()


def test_view_cars_redirection(logged_in_page):
    page = logged_in_page
    print(page.content())
    page.get_by_role("link", name="View All").click()
    expect(page).to_have_title("Your Cars")
