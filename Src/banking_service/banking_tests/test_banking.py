"""Test File for Banking Service"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from banking_service.banking import app, get_db
from banking_service.models import Base

TEST_DB_URL = "sqlite+pysqlite:///:memory:"
engine = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
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

def bank_account_details_payload(banking_id=1, name="John", email="John@Example.com", pin=1225, card="1000000000000000", balance=2):
    return {"banking_id": banking_id, "name": name, "email": email, "pin": pin, "card": card, "balance": balance}

def test_create_bank_account_ok(client):
    """tests if you can successfully create a user"""
    result = client.post("/api/banking", json=bank_account_details_payload())
    assert result.status_code == 201
    data = result.json()
    assert data["banking_id"] == 1
    assert data["name"] == "John"

def test_duplicate_banking_id_conflict(client):
    """tests you can't create a user with an existing id"""
    client.post("/api/banking", json=bank_account_details_payload(banking_id=2))
    result = client.post("/api/banking", json=bank_account_details_payload(banking_id=2))
    assert result.status_code == 409 # duplicate id -> conflict
    assert "exists" in result.json()["detail"].lower()

def test_get_banking_details_404(client):
    """tests 404 is thrown when a user does not exist when trying to get them"""
    result = client.get("/api/banking/999")
    assert result.status_code == 404

def test_delete_then_404(client):
    """tests 404 is throw when trying to delete a user who does not exist"""
    client.post("/api/banking", json=bank_account_details_payload(banking_id=10))
    result1 = client.delete("/api/delete/banking/10")
    assert result1.status_code == 204
    result2 = client.delete("/api/delete/banking/10")
    assert result2.status_code == 404

def test_edit_account_details_ok(client):
    """tests you can edit an existing user"""
    client.post("/api/banking", json=bank_account_details_payload(banking_id=2))
    result1 = client.put("/api/banking/2", json=bank_account_details_payload(banking_id=2, name="Jill"))
    assert result1.status_code == 200
    result2 = client.get("/api/banking/2")
    data = result2.json()
    assert data["name"] == "Jill"

def test_edit_account_details_404(client):
    """tests you can't edit a user that does not exist"""
    result = client.put("/api/banking/2", json=bank_account_details_payload(name="Jill"))
    assert result.status_code == 404

@pytest.mark.parametrize("bad_email", ["BADEMAIL123", "@123.ie", "BAD@", "badmail"])
def test_bad_email_422(client, bad_email):
    """tests invalid user ids throw 422 error"""
    result = client.post("/api/banking", json=bank_account_details_payload(email=bad_email))
    assert result.status_code == 422 # pydantic validation error

@pytest.mark.parametrize("bad_pin", ["BADPIN123", 12345,-2, 999, "@!?"])
def test_bad_pin_422(client, bad_pin):
    """tests invalid user ids throw 422 error"""
    result = client.post("/api/banking", json=bank_account_details_payload(pin=bad_pin))
    assert result.status_code == 422 # pydantic validation error

@pytest.mark.parametrize("bad_card", ["BADEMAIL123", "@123.ie", "BAD@", "badmail",-2, 0,1000000000000000])
def test_bad_card_422(client, bad_card):
    """tests invalid user ids throw 422 error"""
    result = client.post("/api/banking", json=bank_account_details_payload(card=bad_card))
    assert result.status_code == 422 # pydantic validation error

@pytest.mark.parametrize("bad_balance", ["1BAL", -2, "balance"])
def test_bad_balance_422(client, bad_balance):
    """tests invalid user ids throw 422 error"""
    result = client.post("/api/banking", json=bank_account_details_payload(balance=bad_balance))
    assert result.status_code == 422 # pydantic validation error
