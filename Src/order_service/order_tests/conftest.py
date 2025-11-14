"""Order test configs"""

import pytest
from fastapi.testclient import TestClient
from Src.order_service.orders import app

@pytest.fixture
def client():
    return TestClient(app)