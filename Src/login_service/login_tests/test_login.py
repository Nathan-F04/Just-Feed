"""Test File for Login Service"""

def user_payload(name="John", email="john@example.com", password="password"):
    """Builder for login accounts object"""
    return {"name": name, "email": email, "password": password}

def test_create_account_ok(client):
    """Tests post method for creating an account"""
    result = client.post("/api/login/sign-up", json=user_payload())
    assert result.status_code == 201
    data = result.json()
    assert data["id"] == 1
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"
    assert data["password"] == "password"

def test_create_account_409(client):
    """Tests 409 on duplicate account creation"""
    client.post("/api/login/sign-up", json=user_payload())
    result = client.post("/api/login/sign-up", json=user_payload())
    assert result.status_code == 409

def test_login_ok(client):
    client.post("/api/login/sign-up", json=user_payload())
    result = client.post("/api/login/sign-in", json={"email": "john@example.com", "password": "password"})
    assert result.status_code == 200

def test_login_inncorect_password(client):
    client.post("/api/login/sign-up", json=user_payload())
    result = client.post("/api/login/sign-in", json={"email": "john@example.com", "password": "passstesttsxujr"})
    assert result.status_code == 400

def test_login_404(client):
    result = client.post("/api/login/sign-in", json={"email": "john@eample.com", "password": "password"})
    assert result.status_code == 404