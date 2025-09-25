"""Test File for Login Service"""

import pytest
from login_service import create_account

@pytest.fixture(scope="function")
def create_account_test():
    """Test post method for creating an account"""
    account = {
        "user_id" : 1,
        "name" : "testuser",
        "email" : "test@example.com",
        "password" : "testPass1",
    }
    assert create_account(account) == account
