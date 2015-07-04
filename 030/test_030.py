from eul030 import sum_powers

def test_sum_power():
    inputs = [(1634, 4), (8208, 4), (9474, 4)]
    results = [1634, 8208, 9474]
    for i, val in enumerate(inputs):
        assert(sum_powers(*val) == results[i])