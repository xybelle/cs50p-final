from plates import is_valid


def test_starts_w_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("A150") == False


def test_max_chars():
    assert is_valid("AAA222") == True
    assert is_valid("A23456") == False
    assert is_valid("AA123456") == False


def test_number_in_middle():
    assert is_valid("AAA22A") == False
    assert is_valid("AA0123") == False


def test_only_alnum():
    assert is_valid("AAA.12") == False
    assert is_valid("AA 123") == False
