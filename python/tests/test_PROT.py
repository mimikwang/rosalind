from rosalind import PROT

class TestTranslate:
    def test_example_from_site(self):
        sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

        expected = "MAMAPRTEINSTRING"
        actual = PROT.translate(sequence)

        assert actual == expected