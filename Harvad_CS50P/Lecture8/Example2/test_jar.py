from jar import Jar

def test_deposit_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    jar.withdraw(3)
    assert jar.size == 2


def test_str_representation():
    jar = Jar()
    jar.deposit(8)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪'
