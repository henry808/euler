from eul019 import is_leap_year


def test_is_leap_year():
    input_true = [1904, 1908, 1912, 2000, 2004]
    input_false = [1900, 1901, 1902, 1903, 1905]
    for i in input_true:
        assert( is_leap_year(i) == True)
    for i in input_false:
        assert( is_leap_year(i) == False)