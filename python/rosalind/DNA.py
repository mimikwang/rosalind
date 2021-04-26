"""Counting DNA Nucleotides

http://rosalind.info/problems/dna/
"""


def count_nucleotides(sequence: str) -> tuple:
    """Count DNA nucleotides given a sequence

    Args:
        sequence (str): DNA sequence

    Returns:
        tuple: (count of A, count of C, count of G, count of T)
    """
    counter = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in sequence:
        if base in counter.keys():
            counter[base] += 1
    
    return tuple(counter.values())


def load_dataset(file_handle) -> str:
    sequence = file_handle.readline()
    return sequence


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Counting DNA Nucleotides")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequence = load_dataset(f)
    
    output = count_nucleotides(sequence)
    print(output)
