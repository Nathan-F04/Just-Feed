"""Test File for Order Service"""

import pytest
from fastapi.testclient import TestClient

def cart_item_payload(item_name="Pizza", price=12.99, quantity=2):
    return {"item_name": item_name, "price": price, "quantity": quantity}

def test_add_item_to_cart(client):
    """Test adding item to cart"""
    result = client.post("/api/cart/1/items", json=cart_item_payload())
    assert result.status_code == 201
    data = result.json()
    assert data["item_name"] == "Pizza"
    assert data["quantity"] == 2

def test_get_cart(client):
    """Test getting cart"""
    client.post("/api/cart/1/items", json=cart_item_payload())
    result = client.get("/api/cart/1")
    assert result.status_code == 200
    data = result.json()
    assert data["user_id"] == 1
    assert len(data["items"]) == 1

def test_create_order_from_cart(client):
    """Test creating order from cart"""
    client.post("/api/cart/1/items", json=cart_item_payload())
    result = client.post("/api/orders/1")
    assert result.status_code == 201
    data = result.json()
    assert data["user_id"] == 1
    assert data["total_amount"] == 25.98
    assert data["status"] == "pending"

def test_create_order_empty_cart(client):
    """Test creating order with empty cart fails"""
    result = client.post("/api/orders/1")
    assert result.status_code == 400

def test_update_order_status(client):
    """Test updating order status"""
    client.post("/api/cart/1/items", json=cart_item_payload())
    order_result = client.post("/api/orders/1")
    order_id = order_result.json()["id"]
    
    result = client.patch(f"/api/orders/{order_id}/status", json={"status": "confirmed"})
    assert result.status_code == 200
    assert result.json()["status"] == "confirmed"

@pytest.mark.parametrize("bad_price", [-1, 0, "invalid"])
def test_invalid_price_422(client, bad_price):
    """Test invalid price throws 422"""
    result = client.post("/api/cart/1/items", json=cart_item_payload(price=bad_price))
    assert result.status_code == 422

@pytest.mark.parametrize("bad_quantity", [0, -1, "invalid"])
def test_invalid_quantity_422(client, bad_quantity):
    """Test invalid quantity throws 422"""
    result = client.post("/api/cart/1/items", json=cart_item_payload(quantity=bad_quantity))
    assert result.status_code == 422