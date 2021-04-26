from rosalind import RNA


class TestTranscribe:
    def test_example_from_site(self):
        dna_sequence = "GATGGAACTTGACTACGTAAATT"
        
        expected = "GAUGGAACUUGACUACGUAAAUU"
        actual = RNA.transcribe(dna_sequence)

        assert actual == expected
