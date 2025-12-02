from playwright.sync_api import expect


def test_view_cars_redirection(logged_in_page):
    page = logged_in_page
    page.get_by_role("button", name="View All").click()
    expect(page.get_by_role("button", name="Add Car", exact=True)).to_be_visible()
