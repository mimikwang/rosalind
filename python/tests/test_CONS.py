from rosalind import CONS


class TestTransformSequences:
    def test_normal(self):
        sequences = ["AAA", "CCC", "GGT"]
        
        actual = CONS.transform_sequences(sequences)
        expected = [["A", "C", "G"], ["A", "C", "G"], ["A", "C", "T"]]

        assert actual == expected


class TestCalculateProfile:
    def test_normal(self):
        transformed_sequences = [["A", "C", "G"], ["A", "C", "G"], ["A", "C", "T"]]

        actual = CONS.calculate_profile(transformed_sequences)
        expected = [[1, 1, 1], [1, 1, 1], [1, 1, 0], [0, 0, 1]]

        assert actual == expected


class TestGetConsensus:
    def test_normal(self):
        profile = [[1, 0, 0], [1, 2, 0], [1, 1, 0], [0, 0, 1]]

        actual = CONS.get_consensus(profile)
        expected = "ACT"

        assert actual == expected
