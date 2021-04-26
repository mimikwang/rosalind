"""Transcribing DNA into RNA

http://rosalind.info/problems/rna/
"""


def transcribe(dna_sequence: str) -> str:
    """Transcribe DNA to RNA

    Args:
        dna_sequence (str): sequence with DNA nucleotides

    Returns:
        str: RNA sequence
    """
    rna_sequence = []
    for base in dna_sequence:
        if base == "T":
            rna_sequence.append("U")
        else:
            rna_sequence.append(base)
    
    rna_sequence = "".join(rna_sequence)
    return rna_sequence


def load_dataset(file_handle) -> str:
    sequence = file_handle.readline()
    return sequence


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Transcribing DNA into RNA")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequence = load_dataset(f)
    
    output = transcribe(sequence)
    print(output)
