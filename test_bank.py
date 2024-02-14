from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("how do you do") == 20


def test_others():
    assert value("what's up?") == 100
    assert value("you good") == 100


def test_case():
    assert value("ARE YOU OK") == 100
