from twttr import shorten


def test_shorten():
    assert shorten("how are you") == "hw r y"
