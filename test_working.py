from working import convert


def test_am_am():
    assert convert("9 AM to 3 AM") == "09:00 to 03:00"
    assert convert("9:30 AM to 3:30 AM") == "09:30 to 03:30"


def test_am_pm():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"


def test_pm_pm():
    assert convert("1 PM to 9 PM") == "13:00 to 21:00"
    assert convert("1:30 PM to 9:30 PM") == "13:30 to 21:30"
