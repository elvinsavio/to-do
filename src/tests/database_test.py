import os
from database import get_existing_db, create_db
import pytest


@pytest.fixture
def setup_data():
    db_dir = ".db"
    db_name = "test_db"

    print("\nSetting up resources...")
    yield db_name

    os.remove(f"{db_dir}/{db_name}.sqlite3")
    os.rmdir(db_dir)


def test_create_and_get_db(setup_data):
    db_name = setup_data  # Access db_name from the fixture

    result = create_db(db_name)
    assert result == "ok"

    result = create_db(db_name)
    assert result == "already_exists"

    result = get_existing_db()
    assert result == [db_name]
