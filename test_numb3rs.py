from numb3rs import validate, max_255

def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("275.1.1.1") == False


def test_max_255():
    assert max_255("256.255.255.255") == False
    assert max_255("255.255.255.255") == True
    assert max_255("1.1.1.1") == True
    assert max_255("cat") == False
