"""Test File for Profile Setting Service This is a test file that will be removed"""

from src.profile_service.profile import settings

def user_payload(uid=1, name="John", email="john@example.com", password="gywefiyvweyvwueiyf"):
    """Builder for login accounts object"""
    return {"account_id": uid, "name": name, "email": email, "password": password}

def test_update_account_ok(client):
    """Test post method for updating an account"""
    client.post("/api/users", json=user_payload())
    result = client.put("/api/users/1", json=user_payload(name="steve"))
    assert result.status_code == 200
    data = result.json()
    assert data["account_id"] == 1
    assert data["name"] == "steve"
    assert data["email"] == "john@example.com"
    assert data["password"] == "gywefiyvweyvwueiyf"
    settings.clear()

def test_update_account_404(client):
    """Tests cant update an account that does not exist"""
    client.post("/api/users", json=user_payload())
    result = client.put("/api/users/1", json=user_payload(name="steve"))
    assert result.status_code == 200
    data = result.json()
    assert data["account_id"] == 1
    assert data["name"] == "steve"
    assert data["email"] == "john@example.com"
    assert data["password"] == "gywefiyvweyvwueiyf"
    settings.clear()

def test_add_account_ok(client):
    """Test post method for creating an account"""
    result = client.post("/api/users", json=user_payload())
    assert result.status_code == 201
    data = result.json()
    assert data["account_id"] == 1
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"
    assert data["password"] == "gywefiyvweyvwueiyf"
    settings.clear()

def test_add_account_409(client):
    """Test post cant create multipule accounts with same id"""
    client.post("/api/users", json=user_payload())
    result = client.post("/api/users", json=user_payload())
    assert result.status_code == 409
    settings.clear()
