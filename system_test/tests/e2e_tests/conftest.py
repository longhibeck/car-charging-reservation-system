import os
import pytest
from sqlalchemy import create_engine, text


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://test_user:test_password@localhost:5432/car_charging",
)

engine = create_engine(DATABASE_URL)


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
