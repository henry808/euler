from eul033 import cancellable, remove_from


def test_cancellable():
    inputs = [(12, 32),
              (21, 23),
              (12, 987654321),
              (89, 987654321),
              (123546789, 987654321),
              (1, 12345),
              (10, 12),
              (12345, 6789)]
    results = [[2],
               [2],
               [1, 2],
               [8, 9],
               [1, 2, 3, 4, 5, 6, 7, 8, 9],
               [],
               [],
               []]
    for ind, val in enumerate(inputs):
        assert(sorted(cancellable(*val)) == results[ind])


def test_remove_from():
    inputs = [(12, 1), (21, 1), (22, 2), (12, 3)]
    results = [2, 2, 2, 12]
    for ind, val in enumerate(inputs):
        assert(remove_from(*val) == results[ind])