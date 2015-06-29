from eul004 import ith_digit, is_palindrome, find_palindromic


def test_ithdigit():
    n = 12345
    results = [5, 4, 3, 2, 1]
    for i in range(len(results)):
        assert(ith_digit(n, i) == results[i])
    n = 10
    results = [0, 1]
    for i in range(len(results)):
        assert(ith_digit(n, i) == results[i])


def test_ispalindrome():
    input_false = [10, 102, 1121, 1112]
    input_true = [1, 11, 101, 111, 1111, 1221]
    for i in input_false:
        assert(is_palindrome(i) is False)
    for i in input_true:
        assert(is_palindrome(i) is True)