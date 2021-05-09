from rosalind import IEV


class TestExpectedOffsprings:
    def test_example_from_site(self):
        couples = [1, 0, 0, 1, 0, 1]

        actual = IEV.expected_offsprings(couples)
        expected = 3.5

        assert actual == expected

