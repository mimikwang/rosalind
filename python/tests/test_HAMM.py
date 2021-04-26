import io
from rosalind import HAMM


class TestHammingDistance:
    def test_example_from_site(self):
        sequence1 = "GAGCCTACTAACGGGAT"
        sequence2 = "CATCGTAATGACGGCCT"

        actual = HAMM.hamming_distance(sequence1, sequence2)
        expected = 7

        assert actual == expected


class TestLoadData:
    def test_normal(self):
        input_bytes = "GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT\n"
        file_handle = io.StringIO(input_bytes)

        actual = HAMM.load_dataset(file_handle)
        expected = ("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")

        assert actual == expected
