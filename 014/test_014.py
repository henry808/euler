from eul014fast import generate_sequence_length, generate_sequence_length_table


def test_generate_sequence_length():
    expected_lengths = [1, 2, 8, 3, 6, 9, 17, 4, 20, 7]
    for i in range(1, 11):
        assert(generate_sequence_length(i) == expected_lengths[i - 1])


def test_table():
    expected_table = {1: 1,
                      2: 2,
                      3: 8,
                      4: 3,
                      5: 6,
                      6: 9,
                      7: 17,
                      8: 4,
                      9: 20,
                      10: 7}
    assert(generate_sequence_length_table(10) == expected_table)
