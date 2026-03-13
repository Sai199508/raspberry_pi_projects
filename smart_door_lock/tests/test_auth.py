from smart_door_lock.auth_service import AuthService


def test_valid_pin():

    auth = AuthService("1234")

    assert auth.authenticate("1234") == True


def test_invalid_pin():

    auth = AuthService("1234")

    assert auth.authenticate("0000") == False