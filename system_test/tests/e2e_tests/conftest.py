import os
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext, Page
from sqlalchemy import create_engine, text

from system_test.core.clients.client_factory import ClientFactory
from system_test.core.clients.system.api.car_charging_reservation_api_client import CarChargingReservationApiClient
from system_test.core.clients.system.ui.car_charging_reservation_ui_client import CarChargingReservationUiClient
from system_test.core.clients.system.ui.pages.home_page import HomePage


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://test_user:test_password@localhost:5432/car_charging",
)

engine = create_engine(DATABASE_URL)


@pytest.fixture
def logged_in_page(page: Page, base_url) -> Page:
    page.goto(base_url)
    page.get_by_label("Username").fill("addisonw")
    page.get_by_label("Password").fill("addisonwpass")
    page.get_by_role("button", name="Login").click()
    return page


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright, base_url
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url=base_url,
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session")
def logged_in_api_context(
    playwright: Playwright, base_url: str
) -> Generator[APIRequestContext, None, None]:
    login_data = {"username": "addisonw", "password": "addisonwpass"}
    request_context = playwright.request.new_context()
    response = request_context.post(f"{base_url}/api/v1/auth/login", data=login_data)

    if response.status != 200:
        print(f"LOGIN FAILED! Status: {response.status}")
        print(f"Response: {response.text()}")
        raise Exception(f"Login failed with status {response.status}")

    response_json = response.json()
    access_token = response_json["access_token"]

    auth_headers = {"Authorization": f"Bearer {access_token}"}
    authed_context = playwright.request.new_context(
        base_url=base_url, extra_http_headers=auth_headers
    )

    yield authed_context

    authed_context.dispose()
    request_context.dispose()


@pytest.fixture(scope="session")
def charging_points_base_url():
    """Base URL for the charging points service"""
    return os.getenv("CHARGING_POINTS_URL", "http://localhost:8081")


@pytest.fixture(scope="session")
def charging_points_api_context(
    playwright: Playwright, charging_points_base_url: str
) -> Generator[APIRequestContext, None, None]:
    """API context for charging points service"""
    request_context = playwright.request.new_context(base_url=charging_points_base_url)
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="function", autouse=True)
def clean_db():
    """Clean database by deleting all data from all user tables after each test"""
    yield  # Run the test first

    # Clean up after test - loop over all tables and delete data (PRESERVE the test user)
    try:
        with engine.connect() as connection:
            # Get all table names from the public schema, excluding system tables
            result = connection.execute(
                text("""
                SELECT tablename 
                FROM pg_tables 
                WHERE schemaname = 'public' 
                AND tablename NOT LIKE 'alembic%'
                AND tablename NOT LIKE 'pg_%'
                AND tablename NOT LIKE 'sql_%'
            """)
            )

            tables = [row[0] for row in result]

            if tables:
                # Disable foreign key constraints temporarily to avoid deletion order issues
                connection.execute(text("SET session_replication_role = replica;"))

                # Delete data from all tables BUT preserve the test user
                for table in tables:
                    if table == "users":
                        # Keep the test user, delete any other users
                        connection.execute(
                            text("DELETE FROM users WHERE username != 'addisonw'")
                        )
                        print(f"Cleaned table: {table} (preserved test user)")
                    else:
                        # Delete all data from other tables (cars, reservations, etc.)
                        connection.execute(text(f"DELETE FROM {table}"))
                        print(f"Cleaned table: {table}")

                # Re-enable foreign key constraints
                connection.execute(text("SET session_replication_role = DEFAULT;"))

                connection.commit()
                print(f"Successfully cleaned {len(tables)} tables")

    except Exception as e:
        print(f"Clean DB error: {e}")
        # Don't fail the test if cleanup fails
        pass


@pytest.fixture
def car_charging_reservation_ui_client(page: Page) -> CarChargingReservationUiClient:
    return ClientFactory.create_car_charging_reservation_ui_client(page)

@pytest.fixture
def car_charging_reservation_api_client() -> CarChargingReservationApiClient:
    return ClientFactory.create_car_charging_reservation_api_client()


@pytest.fixture
def authenticated_api_client() -> CarChargingReservationApiClient:
    """
    Fixture that provides an authenticated API client.
    Logs in and sets the auth token for subsequent requests.
    """
    api_client = ClientFactory.create_car_charging_reservation_api_client()
    
    # Login to get token
    response = api_client.auth().login(username="addisonw", password="addisonwpass")
    auth_data = api_client.auth().assert_login_successful(response)
    access_token = auth_data["access_token"]
    
    # Set auth token for all controllers
    api_client.http_client.set_auth_token(access_token)
    
    return api_client


# Analyse usage
@pytest.fixture
def authenticated_home_page(car_charging_reservation_ui_client: CarChargingReservationUiClient) -> HomePage:
    """
    Fixture that provides an authenticated home page.
    Use this when you need to start tests from the home page.
    """
    login_page = car_charging_reservation_ui_client.navigate_to_home()
    home_page = login_page.login(username="addisonw", password="addisonwpass")
    return home_page