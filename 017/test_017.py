from eul017 import number2word

def test_number2word():
    input_numbers = [1, 19, 20, 21, 99, 100, 101, 919, 999, 1101, 9990, 9999]
    expected_result = ['one', 'nineteen', 'twenty', 'twenty one',
                       'ninety nine', 'one hundred', 'one hundred one',
                       'nine hundred nineteen', 'nine hundred ninety nine',
                       'one thousand one hundred one',
                       'nine thousand nine hundred ninety',
                       'nine thousand nine hundred ninety nine']
    for i, n in enumerate(input_numbers):
        assert(number2word(n) == expected_result[i])