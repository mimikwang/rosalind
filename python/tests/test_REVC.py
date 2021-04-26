from rosalind import REVC


class TestReverseComplement:
    def test_example_from_site(self):
        sequence = "AAAACCCGGT"

        expected = "ACCGGGTTTT"
        actual = REVC.reverse_complement(sequence)

        assert actual == expected
