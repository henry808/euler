from eul019 import is_leap_year, days_in_months


def test_is_leap_year():
    input_true = [1904, 1908, 1912, 2000, 2004]
    input_false = [1900, 1901, 1902, 1903, 1905]
    for i in input_true:
        assert( is_leap_year(i) == True)
    for i in input_false:
        assert( is_leap_year(i) == False)


def test_days_in_months():
    input_months =[(1, 1900),
                   (2, 1900),
                   (3, 1900),
                   (4, 1900),
                   (5, 1900),
                   (6, 1900),
                   (7, 1900),
                   (8, 1900),
                   (9, 1900),
                   (10, 1900),
                   (11, 1900),
                   (12, 1900),
                   (2, 1904)
                   ]
    expected = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31, 29]

    for ind, val in enumerate(input_months):
        assert( days_in_months(*val)== expected[ind])