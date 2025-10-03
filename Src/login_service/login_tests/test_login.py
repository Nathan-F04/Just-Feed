"""Test File for Login Service"""

from src.login_service.login import accounts

def user_payload(uid=1, name="John", email="john@example.com", password="password"):
    """Builder for login accounts object"""
    return {"user_id": uid, "name": name, "email": email, "password": password}

def test_create_account_ok(client):
    """Tests post method for creating an account"""
    result = client.post("/account/create", json=user_payload())
    assert result.status_code == 201
    data = result.json()
    assert data["user_id"] == 1
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"
    assert data["password"] == "password"
    accounts.clear()

def test_create_account_409(client):
    """Tests 409 on duplicate account creation"""
    client.post("/account/create", json=user_payload())
    result = client.post("/account/create", json=user_payload())
    assert result.status_code == 409
    accounts.clear()
