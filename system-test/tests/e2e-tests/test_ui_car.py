from playwright.sync_api import expect


def test_add_car_ui(logged_in_page):
    # Log in
    page = logged_in_page

    # Go to car page
    page.get_by_role("button", name="View All").click()

    # Go to add car page
    page.get_by_role("button", name="Add Car", exact=True).click()

    # Fill in the add car form
    page.locator("#car-name").fill("Test Car")

    page.locator("#connector-TYPE_2").check()

    page.locator("#battery-charge-limit").fill("80")
    page.locator("#battery-size").fill("60")
    page.locator("#max-kw-ac").fill("11")
    page.locator("#max-kw-dc").fill("50")

    # Submit the form
    page.get_by_role("button", name="Add Car", exact=True).click()

    # More specific: check the car appears in a table row
    expect(page.get_by_role("cell", name="Test Car")).to_be_visible()
    expect(page.get_by_role("cell", name="60")).to_be_visible()
    expect(page.get_by_role("cell", name="11")).to_be_visible()
    expect(page.get_by_role("cell", name="50")).to_be_visible()
