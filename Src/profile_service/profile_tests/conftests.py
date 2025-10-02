"""Profile test configs"""

from fastapi.testclient import TestClient
from profile_service.profile_service import app
import pytest

@pytest.fixture
def client():
    """Creates a new instance of App"""
    return TestClient(app)
