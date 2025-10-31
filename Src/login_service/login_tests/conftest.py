"""Login test configs"""

from fastapi.testclient import TestClient
from Src.login_service.login import app, get_db
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Src.login_service.models import Base

TEST_DB_URL = "sqlite+pysqlite:///:memory:"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    """Creates a new instance of App"""
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
            app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        # hand the client to the test
        yield c
        # --- teardown happens when the 'with' block exits ---
