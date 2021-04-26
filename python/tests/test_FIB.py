from rosalind import FIB


class TestCountRabbits:
    def test_first_iteration(self):
        previous = 1
        current = 1
        k = 3

        expected = 4
        actual = FIB.count_rabbits(previous, current, k)

        assert actual == expected

    def test_second_iteration(self):
        previous = 1
        current = 4
        k = 3

        expected = 7
        actual = FIB.count_rabbits(previous, current, k)

        assert actual == expected

    def test_third_iteration(self):
        previous = 4
        current = 7
        k = 3

        expected = 19
        actual = FIB.count_rabbits(previous, current, k)

        assert actual == expected


class TestRecursiveCount:
    def test_example_from_site(self):
        n = 5
        k = 3

        expected = 19
        actual = FIB.recursive_count(n, k)

        assert actual == expected

