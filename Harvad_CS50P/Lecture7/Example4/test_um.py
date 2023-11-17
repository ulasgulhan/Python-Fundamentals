from um import count

def test_word_count():
    assert count("Um um um um") == 4
    assert count("Umm, yeah, um") == 2
    assert count("This is a test") == None

def test_case_insensitivity():
    assert count("um UM um") == 3
    assert count("UM UM") == 2

def test_word_boundaries():
    assert count("drum, drummer, hum, um") == 1
    assert count("dummy, dummyum, um") == 1