from playwright.sync_api import expect


def test_dashboard(logged_in_page):
    page = logged_in_page
    expect(page.get_by_text("Your Reservations")).to_be_visible()
    # Use more specific selector to avoid duplicate "Your Cars" headings
    expect(
        page.locator("section").filter(has_text="Your Cars").get_by_role("heading")
    ).to_be_visible()


def test_view_cars_redirection(logged_in_page):
    page = logged_in_page
    # Fix: "View All" is a button, not a link
    page.get_by_role("button", name="View All").click()
    # Fix: "Add Car" is also a button, not a link
    expect(page.get_by_role("button", name="Add Car", exact=True)).to_be_visible()
