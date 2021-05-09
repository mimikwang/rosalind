from rosalind import LCSM


class TestChopSequence:
    def test_example(self):
        sequence = "AAAT"

        actual = LCSM.chop_sequence(sequence)
        expected = {"AA", "AT", "AAA", "AAT", "AAAT"}

        assert actual == expected


class TestFindSharedMotifs:
    def test_example(self):
        sequences = ["ATAA", "AAT", "TAAT"]

        actual = LCSM.find_shared_motifs(sequences)
        expected = {"AA", "AT"}

        assert actual == expected


class TestGetLongestMotif:
    def test_example(self):
        motifs = {"AAAAA", "ACT", "TTT", "CCCAGT"}
        actual = LCSM.get_longest_motif(motifs)
        expected = "CCCAGT"

        assert actual == expected


class TestFindLongestSharedMotif:
    def test_example_from_site(self):
        sequences = ["GATTACA", "TAGACCA", "ATACA"]
        actual = LCSM.find_longest_shared_motif(sequences)
        expected = "AC"

        assert actual == expected
