from leapyear import is_leap_year

def test_normal_years():
    assert not is_leap_year(1)
    assert not is_leap_year(2001)
    assert not is_leap_year(2017)
    assert not is_leap_year(2021)

def test_multiples_of_4():
    assert is_leap_year(4)
    assert is_leap_year(2008)
    assert is_leap_year(2020)

def test_multiples_of_100():
    assert not is_leap_year(100)
    assert not is_leap_year(2100)
    assert not is_leap_year(1900) # i'm looking at you, microsoft excel

def test_multiples_of_400():
    assert is_leap_year(1600)
    assert is_leap_year(2000)
    assert is_leap_year(2400)
