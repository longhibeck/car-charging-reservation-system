from playwright.sync_api import expect


def test_should_login(logged_in_page):
    page = logged_in_page
    expect(page.get_by_role("heading", name="Your Reservations")).to_be_visible()
    expect(page.get_by_role("heading", name="Your Cars")).to_be_visible()


def test_should_not_login_with_invalid_credentials(page, base_url):
    page.goto(base_url)
    page.get_by_label("Username").fill("invalid_user")
    page.get_by_label("Password").fill("invalid_pass")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Login failed")).to_be_visible()


def test_should_not_login_with_missing_fields(page, base_url):
    page.goto(base_url)
    page.get_by_role("button", name="Login").click()
    page.get_by_label("Username").fill("user")
    password_field = page.get_by_label("Password")
    validation_message = password_field.evaluate("element => element.validationMessage")
    assert validation_message == "Please fill out this field."
