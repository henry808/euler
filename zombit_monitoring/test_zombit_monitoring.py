from zombit_monitoring import answer


def test_zombit_monitoring():
    intervals = [[[1, 2], [5, 6]], [[1, 3], [3, 6]], [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]]
    expected = [2, 5, 16]
    for ind, val in enumerate(intervals):
        assert(answer(val) == expected[ind])