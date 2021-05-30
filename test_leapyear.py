from leapyear import is_leap_year

def test_normal_years():
    assert not is_leap_year(1)
    assert not is_leap_year(2001)
    assert not is_leap_year(2017)
    assert not is_leap_year(2021)
