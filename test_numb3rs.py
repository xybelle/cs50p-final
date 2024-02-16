from numb3rs import validate


def test_in_range():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("275.1.1.1") == False
    assert validate("255.276.255.255") == False
    assert validate("255.255.265.255") == False
    assert validate("255.255.255.285") == False


def test_four_sets():
    assert validate("1.1.1.1.1") == False
    assert validate("1.1.1.1") == True


def test_only_digits():
    assert validate("cat") == False
