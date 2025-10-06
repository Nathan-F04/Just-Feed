"""Test File for Profile Setting Service"""
import pytest
from profile_service.profile_service import update_account


@pytest.fixture(scope="function")
def update_account_test():
    """Test post method for updating an account"""
    account = {
        "user_id" : 1,
        "name" : "testuser",
        "email" : "test@example.com",
        "password" : "testPass1",
    }
    assert update_account(account) == account
    