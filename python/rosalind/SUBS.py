"""Finding a Motif in DNA

http://rosalind.info/problems/subs/
"""


def motif_locations(sequence: str, motif: str) -> list:
    """Find motif locations

    Args:
        sequence (str): sequence
        motif (str): motif

    Returns:
        list: starting locations of motif in sequence]
    """
    output = []
    for i in range(len(sequence)-len(motif)):
        subsequence = sequence[i:i+len(motif)]
        if subsequence == motif:
            output.append(str(i + 1))
    return " ".join(output)


def load_dataset(file_handle) -> tuple:
    input_data = file_handle.readlines()
    input_data = [x.replace("\n", "") for x in input_data]
    return input_data[0], input_data[1]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Finding a Motif in DNA")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequence, motif = load_dataset(f)

    output = motif_locations(sequence, motif)
    print(output)
