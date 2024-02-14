from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_h():
    assert value("how do you do") == 20
    assert value("HOW DO YOU DO") == 20


def test_others():
    assert value("what's happening") == 100
    assert value("WHAT'S HAPPENING") == 100


def test_case():
    assert value("ARE YOU OK") == 100
    assert value("are you ok") == 100
