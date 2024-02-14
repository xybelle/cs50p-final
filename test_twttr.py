from twttr import shorten


def test_lowercase():
    assert shorten("how are you") == "hw r y"


def test_uppercase():
    assert shorten("HOW ARE YOU") == "HW R Y"


def test_numbers():
    assert shorten("1 day Two DAys 3 days") == "1 dy Tw Dys 3 dys"


def test_punc():
    assert shorten("Can you hear me?") == "Cn y hr m?"
