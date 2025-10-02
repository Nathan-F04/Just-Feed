"""Test File for Profile Setting Service"""

def user_payload(uid=1, name="John", email="john@example.com", age=25, password="gywefiyvweyvwueiyf"):
    """Builder for login accounts object"""
return {"user_id": uid, "name": name, "email": email, "password": password}

def update_account_test():
    """Test post method for updating an account"""
    result = client.post("/api/users")
    assert result.status_code == 200
    data = result.json()
    assert data["user_id"] == 1
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"
    assert data["age"] == 25
    assert data["password"] == "gywefiyvweyvwueiyf"
