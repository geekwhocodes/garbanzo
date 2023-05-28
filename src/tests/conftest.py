


import os
import pytest
from starlette.testclient import TestClient

from app import main
from app.config import Settings, get_settings

def get_settings_override() -> Settings:
    return Settings(env="dev", database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = main.app
    app.dependency_overrides[get_settings] = get_settings_override
    
    with TestClient(app=app) as c:

        #Tests
        yield c
