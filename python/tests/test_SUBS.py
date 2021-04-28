from rosalind import SUBS


class TestFindMotif:
    def test_example_from_site(self):
        sequence = "GATATATGCATATACTT"
        motif = "ATAT"

        actual = SUBS.motif_locations(sequence, motif)
        expected = "2 4 10"

        assert actual == expected
