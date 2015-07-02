from eul020 import factorial

def test_factorial():
    inputs = [1, 3, 10]
    expected = [1 , 6, 3628800]
    for ind, val in enumerate(inputs):
        assert(factorial(val) == expected[ind])