import io
from rosalind import GC


class TestCountGC:
    def test_normal(self):
        sequence = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"

        actual = GC.count_gc(sequence)
        expected = 60.919540
        difference = abs(actual - expected)

        assert difference < 0.001


class TestLoadDataset:
    def test_normal(self):
        input_bytes = ">sequence1\nAAA\nGGG\n>sequence2\nCCC\nTT\n"
        file_handle = io.StringIO(input_bytes)
        
        actual = GC.load_dataset(file_handle)
        expected = [("sequence1", "AAAGGG"), ("sequence2", "CCCTT")]

        assert actual == expected


class TestGetMaxGC:
    def test_example_from_site(self):
        sequences = [
            ("Rosalind_6404", "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"),
            ("Rosalind_5959", "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"),
            ("Rosalind_0808", "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT")
        ]

        actual_name, actual_gc = GC.get_max_gc(sequences)
        expected_name = "Rosalind_0808"
        expected_gc = 60.919540
        difference = abs(actual_gc - expected_gc)

        assert difference < 0.001
        assert actual_name == expected_name
