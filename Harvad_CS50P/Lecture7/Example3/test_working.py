from working import convert

def test_valid_conversion():
    assert convert("1:30 PM to 5:45 PM") == "13:30 to 17:45"
    assert convert("12:00 AM to 11:59 PM") == "00:00 to 23:59"
    assert convert("10:15 AM to 3:30 PM") == "10:15 to 15:30"

def test_invalid_hour():
    try:
        convert("15:30 PM to 6:45 PM")
    except ValueError:
        assert True

def test_invalid_format():
    try:
        convert("3:30 PM to 6:45 PM")
    except ValueError:
        assert True

def test_invalid_am_pm():
    try:
        convert("3:30 XM to 6:45 PM")
    except ValueError:
        assert True