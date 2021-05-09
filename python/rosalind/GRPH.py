"""Overlap Graphs

http://rosalind.info/problems/grph/
"""
import itertools as it


def get_prefix(sequence: str, k: int) -> str:
    """Return the prefix of length k

    Args:
        sequence (str): sequence
        k (int): prefix length

    Returns:
        str: the prefix
    """
    return sequence[:k]


def get_suffix(sequence: str, k: int) -> str:
    """Return the suffix of length k

    Args:
        sequence (str): sequence
        k (int): suffix length

    Returns:
        str: the suffix
    """
    return sequence[-k:]


def get_overlaps(sequences: list, k: int) -> list:
    """Return the overlap graph

    Args:
        sequences (list): a list of tuples where the first element is the sequence name and the second is the sequence
        k (int): prefix and suffix length

    Returns:
        list: overlap graph
    """
    combinations = it.combinations(sequences, 2)
    output = []
    for seq1, seq2 in combinations:
        if get_suffix(seq1[1], k) == get_prefix(seq2[1], k):
            output.append("{} {}".format(seq1[0], seq2[0]))

        if get_prefix(seq1[1], k) == get_suffix(seq2[1], k):
            output.append("{} {}".format(seq2[0], seq1[0]))
    
    return output


def load_dataset(file_handle) -> list:
    """Parse a fasta file

    Args:
        file_handle: file handle to fasta file

    Returns:
        list: a list where each element is a tuple where the first element is the sequence name and the second is the
            sequence
    """
    output = []
    lines = file_handle.readlines()
    name = None
    for line in lines:
        line = line.replace("\n", "")
        if line.startswith(">"):
            if name:
                output.append((name, sequence))
            name = line[1:]
            sequence = ""
        else:
            sequence += line

    if name:
        output.append((name, sequence))
    
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Overlap Graphs")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequences = load_dataset(f)
    
    output = get_overlaps(sequences, 3)
    for sequence in output:
        print(sequence)
