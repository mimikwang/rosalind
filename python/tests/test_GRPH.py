import io
from rosalind import GRPH


class TestGetPrefix:
    def test_example_from_site(self):
        sequence = "AAATAAA"
        
        expected = "AAA"
        actual = GRPH.get_prefix(sequence, 3)

        assert actual == expected


class TestGetSuffix:
    def test_example_from_site(self):
        sequence = "AAATCCC"

        expected = "CCC"
        actual = GRPH.get_suffix(sequence, 3)

        assert actual == expected


class TestGetOverlaps:
    def test_example_from_site(self):
        sequences = [
            ("Rosalind_0498", "AAATAAA"),
            ("Rosalind_2391", "AAATTTT"),
            ("Rosalind_2323", "TTTTCCC"),
            ("Rosalind_0442", "AAATCCC"),
            ("Rosalind_5013", "GGGTGGG")
        ]
        
        actual = GRPH.get_overlaps(sequences, 3)
        print(actual)
        expected = [
            "Rosalind_0498 Rosalind_2391", 
            "Rosalind_0498 Rosalind_0442", 
            "Rosalind_2391 Rosalind_2323"
        ]

        assert actual == expected


class TestLoadDataset:
    def test_example_from_site(self):
        input_bytes = ">Rosalind_0498\nAAATAAA\n" + \
            ">Rosalind_2391\nAAATTTT\n" + \
            ">Rosalind_2323\nTTTTCCC\n" + \
            ">Rosalind_0442\nAAATCCC\n" + \
            ">Rosalind_5013\nGGGTGGG\n"
        file_handle = io.StringIO(input_bytes)

        actual = GRPH.load_dataset(file_handle)
        expected = [
            ("Rosalind_0498", "AAATAAA"),
            ("Rosalind_2391", "AAATTTT"),
            ("Rosalind_2323", "TTTTCCC"),
            ("Rosalind_0442", "AAATCCC"),
            ("Rosalind_5013", "GGGTGGG")
        ]

        assert actual == expected
