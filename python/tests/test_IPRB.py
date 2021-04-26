from rosalind import IPRB


class TestCalculateProbability:
    def test_example_from_site(self):
        k = 2
        m = 2
        n = 2

        expected = 0.7833
        actual = IPRB.calculate_probability(k, m, n)
        difference = abs(expected - actual)

        assert difference < 0.01
