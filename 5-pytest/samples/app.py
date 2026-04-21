def test_addition():
    assert add(3,2) == 5
    assert add(-1,1) == 0

import pytest
@pytest.fixture
def db_connection():
    db = Database.connect()
    yield db
    db.close()

#Parameterized Testing
@pytest.mark.parametrize("user", "password", [("admin", "123"),  ("amritansh_lal,SamPass")])
def test_login_fail(user, password):
    assert login(user, password) == "Access Denied"


@pytest.mark.parametrize("user", "password", [ ("amritansh_lal@gmail.com,Welcome@123")])
def test_login_pass(user, password):
    assert login(user, password) == "Access Granted"
