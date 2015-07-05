#! /usr/bin/python
from __future__ import print_function
from pprint import pprint
from copy import deepcopy

# Project Euler #31
coins = (('1p', 1),
         ('2p', 2),
         ('5p', 5),
         ('10p', 10),
         ('20p', 20),
         ('50p', 50),
         ('L1', 100),
         ('L2', 200))


def total_of_coins(table):
    """ adds up coins in table and returns total"""
    total = 0
    for coin in coins:
        if coin[0] in table:
            total += table[coin[0]] * coin[1]
    return total


def ways_to_make(n):
    """ways to make n using combinations of coins"""
    ways = []
    # can do these next three lines with fromkeys:
    coin_table = {}
    for coin in coins:
        coin_table[coin[0]] = 0
    ways.append(coin_table)
    for coin in reversed(coins):
        coin_ways = deepcopy(ways)  # copy all previous ways
        # possibilities for each coin
        if coin[1] == 1:
            # if 1 cent, then manually calculate what it should be
            for way in ways:
                way[coin[0]] = n - total_of_coins(way)
        else:
            for i in range(1, n / coin[1] + 1):
                # way is a coin table (possiblity)            
                for way in coin_ways:
                    way[coin[0]] = i
                # clean out the ones that are too high to save time
                for way in coin_ways:
                    if total_of_coins(way) > n:
                        coin_ways.remove(way)
                ways = ways + deepcopy(coin_ways)
    # 'ways' now is all possiblities that are not too high

    # compile all that add up to n
    right_ways = []
    for way in ways:
        if total_of_coins(way) == n:
            right_ways.append(way)
    return right_ways


if __name__ == '__main__':
    ways = ways_to_make(200)
    # pprint(ways)
    print(len(ways))