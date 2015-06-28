from eul004 import ith_digit, is_palindrome, find_palindromic


def test_ithdigit():
    n = 12345
    results = [5, 4, 3, 2, 1]
    for i in range(4):
        assert(ith_digit(n, i) == results[i])
