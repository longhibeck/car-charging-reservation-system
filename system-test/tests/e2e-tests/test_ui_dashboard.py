from playwright.sync_api import expect


def test_dashboard(logged_in_page):
    page = logged_in_page
    expect(page.get_by_text("Your Reservations")).to_be_visible()
    expect(page.get_by_text("Your Cars")).to_be_visible()


def test_view_cars_redirection(logged_in_page):
    page = logged_in_page
    print(page.content())
    page.get_by_role("link", name="View All").click()
    expect(page.get_by_role("link", name="Add Car")).to_be_visible()
