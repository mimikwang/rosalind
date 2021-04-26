"""Counting Point Mutations

http://rosalind.info/problems/hamm/
"""


def hamming_distance(sequence1: str, sequence2: str) -> int:
    """Calculating the Hamming distsance between two sequences

    Args:
        sequence1 (str): first sequence
        sequence2 (str): second sequence

    Returns:
        int: the hamming distance
    """
    output = 0
    for base1, base2 in zip(sequence1, sequence2):
        if base1 != base2:
            output += 1
    
    return output


def load_dataset(file_handle) -> tuple:
    input_data = file_handle.readlines()
    input_data = [x.replace("\n", "") for x in input_data]
    return input_data[0], input_data[1]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Counting Point Mutations")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequence1, sequence2 = load_dataset(f)
    
    output = hamming_distance(sequence1, sequence2)
    print(output)
