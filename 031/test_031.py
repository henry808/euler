from eul031 import total_of_coins, ways_to_make


def test_total_of_coins():
    table1 = {'1p': 3,
              '2p': 1,
              '5p': 1,
              '10p': 0,
              '20p': 2,
              '50p': 1,
              'L1': 1,
              'L2': 0}
    assert(total_of_coins(table1) == 200)