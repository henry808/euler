from eul036 import is_palendromic


def test_is_palendromic():
    inputs = [585, 123]
    results = [True, False]
    for ind, val in enumerate(inputs):
        assert(is_palendromic(val) is results[ind])
