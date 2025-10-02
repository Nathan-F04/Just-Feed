"""Test File for Login Service"""

def user_payload(uid=1, name="John", email="john@example.com", password="gywefiyvweyvwueiyf"):
    """Builder for login accounts object"""
    return {"user_id": uid, "name": name, "email": email, "age": age, "password": password}

def test_create_account_ok(client):
    """Test post method for creating an account"""
    result = client.post("/account/create")
    assert result.status_code == 200
    data = result.json()
    assert data["user_id"] == 1
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"
    assert data["password"] == "gywefiyvweyvwueiyf"
