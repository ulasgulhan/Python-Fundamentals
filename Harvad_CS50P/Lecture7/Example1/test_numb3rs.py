from numb3rs import validate

def test_valid_ipv4():
    validate_result = validate("192.168.1.1")
    assert validate_result

def test_invalid_ipv4():
    validate_result = validate("256.0.0.1")
    assert not validate_result