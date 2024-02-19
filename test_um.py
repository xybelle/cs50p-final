import pytest

from um import count


def test_um():
    assert count("um, hello, um, world") == 2
    assert count("yummy") == None
    assert count("um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thnks, um...") == 2
