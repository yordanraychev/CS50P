from jar import Jar

def test_init():
    jar = Jar(7)
    assert jar.capacity == 7
    assert jar.size == 0
    jar1 = Jar()
    assert jar1.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(6)
    assert jar.size == 11


def test_withdraw():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(3)
    assert jar.size == 8
    jar.withdraw(2)
    assert jar.size == 6
