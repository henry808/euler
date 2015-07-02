#! /usr/bin/python
from __future__ import print_function

# Project Euler # 17

digit = [{},{},{},{}]
digit[0] = {0: '',
            1: 'one', 
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen'} 
digit[1] = {20: 'twenty',
            30: 'thirty',
            40: 'fourty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety'}
digit[2] = {100: 'hundred'}
digit[3] = {1000: 'thousand'}

def number2word(n):
    if n == 0:
        return 'zero'
    word = ''
    if n > 999:        
        word += digit[0][n / 1000]
        word += ' thousand '
        n = n % 1000
    if n > 99:
        word += digit[0][n / 100]
        word += ' hundred '
        n = n % 100      
    if n > 19:
        word += digit[1][(n / 10) * 10]
        word += ' '
        n = n % 10
    word += digit[0][n]
    return word.strip()

if __name__ == '__main__':
    print(digit)


