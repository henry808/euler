from eul005 import is_evenly_divisable, divisables
from numpy import prod


def test_is_evenly_divisable():

    input_true = [prod(divisables), 2 * prod(divisables)]
    input_false = [10, 20, 30]
    for i in input_false:
        assert(is_evenly_divisable(i) is False)
    for i in input_true:
        assert(is_evenly_divisable(i) is True)