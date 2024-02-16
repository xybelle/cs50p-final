import numb3rs


def test_validate():
    assert numb3rs.validate("1.2.3.4") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("275.1.1.1") == False
    assert numb3rs.validate("cat") == False





def test_four_sets():
    assert numb3rs.four_sets("1.1.1.1.1") == False
    assert numb3rs.four_sets("1.1.1.1") == True
