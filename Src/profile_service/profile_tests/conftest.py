"""Profile test configs"""

from fastapi.testclient import TestClient
from Src.profile_service.profile import app
import pytest

@pytest.fixture
def client():
    """Creates a new instance of App"""
    return TestClient(app)
