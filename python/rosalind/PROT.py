"""Translating RNA into Protein

http://rosalind.info/problems/prot/
"""
CODON_MAP = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}


def translate(sequence: str) -> str:
    output = []
    chunks = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    for chunk in chunks:
        protein = CODON_MAP.get(chunk)
        if protein == "Stop":
            break

        if protein:
            output.append(protein)
    
    output = "".join(output)
    return output


def load_dataset(file_handle) -> str:
    sequence = file_handle.readline()
    return sequence


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Translate RNA into Protein")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequence = load_dataset(f)

    output = translate(sequence)
    print(output)

