from rosalind import FIBD


class TestRecursiveCount:
    def test_example_from_site(self):
        n = 6
        m = 3

        expected = 4
        actual = FIBD.recursive_count(n, m)

        assert actual == expected
