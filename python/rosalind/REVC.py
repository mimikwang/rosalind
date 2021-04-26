"""Complementing a Strand of DNA

http://rosalind.info/problems/revc/
"""
COMPLEMENT_MAP = {"A": "T", "T": "A", "C": "G", "G": "C"}


def reverse_complement(sequence: str) -> str:
    """Reverse complement a DNA sequence

    Args:
        sequence (str): DNA sequence to be reversed and complemented

    Returns:
        str: the reverse complement
    """
    sequence = list(sequence)
    sequence.reverse()
    
    output = []
    for base in sequence:
        output.append(COMPLEMENT_MAP.get(base, base))
    
    output = "".join(output)
    return output


def load_dataset(file_handle) -> str:
    sequence = file_handle.readline()
    return sequence


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Complementing a Strand of DNA")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequence = load_dataset(f)

    output = reverse_complement(sequence)
    print(output)
    