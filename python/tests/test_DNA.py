from rosalind import DNA


class TestCountNucleotides:
    def test_example_from_site(self):
        sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

        expected = (20, 12, 17, 21)
        actual = DNA.count_nucleotides(sequence)

        assert actual == expected

