"""Login test configs"""

from fastapi.testclient import TestClient
from login_service.login import app
import pytest

@pytest.fixture
def client():
    """Creates a new instance of App"""
    return TestClient(app)
