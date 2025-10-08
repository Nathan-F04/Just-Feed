"""Test File for Banking Service"""

import pytest
from Src.banking_service.banking import bank_details

def bank_account_details_payload(banking_id=1, name="Paul", email="pl@atu.ie", pin=1225, card=1234, balance=2):
    return {"banking_id": banking_id, "name": name, "email": email, "pin": pin, "card": card, "balance": balance}

def test_create_bank_account_ok(client):
    """tests if you can successfully create a user"""
    result = client.post("/api/banking", json=bank_account_details_payload())
    assert result.status_code == 201
    data = result.json()
    assert data["banking_id"] == 1
    assert data["name"] == "Paul"
    bank_details.clear() #clears global list

def test_duplicate_banking_id_conflict(client):
    """tests you can create a user with an existing id"""
    client.post("/api/banking", json=bank_account_details_payload(banking_id=2))
    result = client.post("/api/banking", json=bank_account_details_payload(banking_id=2))
    assert result.status_code == 409 # duplicate id -> conflict
    assert "exists" in result.json()["detail"].lower()
    bank_details.clear()

def test_get_banking_details_404(client):
    """tests 404 is thrown when a user does not exist when trying to get them"""
    result = client.get("/api/banking/999")
    assert result.status_code == 404
    bank_details.clear()

def test_delete_then_404(client):
    """tests 404 is throw when trying to delete a user who does not exist"""
    client.post("/api/banking", json=bank_account_details_payload(banking_id=10))
    result1 = client.delete("/api/delete/banking/10")
    assert result1.status_code == 204
    result2 = client.delete("/api/delete/banking/10")
    assert result2.status_code == 404
    bank_details.clear()

def test_edit_account_details_ok(client):
    """tests you can edit an existing user"""
    client.post("/api/banking", json=bank_account_details_payload(banking_id=2))
    client.post("/api/banking/2", json=bank_account_details_payload())
    result1 = client.put("/api/banking/2", json=bank_account_details_payload(name="pil"))
    print(result1)
    assert result1.status_code == 200
    bank_details.clear()

def test_edit_account_details_404(client):
    """tests you can't edit a user that does not exist"""
    client.post("/api/banking", json=bank_account_details_payload())
    result = client.put("/api/banking/2", json=bank_account_details_payload(name="pil"))
    assert result.status_code == 404
    bank_details.clear()

#bad name

@pytest.mark.parametrize("bad_email", ["BADEMAIL123", "@123.ie", "BAD@", "badmail"])
def test_bad_student_id_422(client, bad_email):
    """tests invalid user ids throw 422 error"""
    result = client.post("/api/banking", json=bank_account_details_payload(email=bad_email))
    assert result.status_code == 422 # pydantic validation error
    bank_details.clear()

#bad pin

#bad card