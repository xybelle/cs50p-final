import seasons
import pytest


def test_sing():
    assert seasons.sing("525600") == "Five hundred twenty-five thousand, six hundred"
    assert seasons.sing("1051200") == "One million, fifty-one thousand, two hundred"


def test_format():
    with pytest.raises(ValueError):
        seasons.get_dob("1989-12")



