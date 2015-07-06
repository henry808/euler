from eul034 import is_special

def test_is_special():
    inputs = [145, 12]
    results = [True, False]
    for ind, val in enumerate(inputs):
        assert(is_special(val) is results[ind])