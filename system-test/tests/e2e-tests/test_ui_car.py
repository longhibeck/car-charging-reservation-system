from playwright.sync_api import expect


def test_add_car_ui(logged_in_page):
    # Log in
    page = logged_in_page

    # Go to car page
    page.get_by_role("link", name="View All").click()

    # Go to add car page
    page.get_by_role("link", name="Add Car").click()

    # Fill in the add car form
    page.locator('input[name="name"]').fill("Test Car")
    page.get_by_role("checkbox", name="Type 2").check()
    page.locator('input[name="battery_charge_limit"]').fill("80")
    page.locator('input[name="battery_size"]').fill("60")
    page.locator('input[name="max_kw_ac"]').fill("11")
    page.locator('input[name="max_kw_dc"]').fill("50")
    page.get_by_role("button", name="Add Car").click()

    # After submission, should redirect to /car or dashboard
    expect(page.get_by_text("Test Car")).to_be_visible()
