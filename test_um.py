import pytest

from um import count


def test_um():
    assert count("um, hello, um, world") == 2
    assert count("yummy") == 0
    assert count("um?") == 1


def test_case_insensitive_um():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2


def test_spaces_around_um():
    assert count("um, um are you sure?") == 2

