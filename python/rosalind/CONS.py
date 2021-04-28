"""Consensus and Profile

http://rosalind.info/problems/cons/
"""


def transform_sequences(sequences: list) -> list:
    """Transform sequences to a list of list

    Args:
        sequences (list): input sequences

    Returns:
        list: a list of list of bases
    """
    transformed = [list(sequence) for sequence in sequences]
    transformed = list(zip(*transformed))
    transformed = [list(s) for s in transformed]

    return transformed


def calculate_profile(transformed_sequences: list) -> dict:
    """Given transformed sequences, calculate the profile

    Args:
        transformed_sequences (list): transformed sequences as output from `transform_sequences`

    Returns:
        list: a list of 4 lists where each list corresponds to A, C, G, and T, respectively.  Each element of the sub
            list is the count of the base at the given index.
    """
    sequence_length = len(transformed_sequences)
    profile = {
        "A": [0] * sequence_length,
        "C": [0] * sequence_length,
        "G": [0] * sequence_length,
        "T": [0] * sequence_length
    }

    for base_index in range(sequence_length):
        for base in transformed_sequences[base_index]:
            profile[base][base_index] += 1
    
    return list(profile.values())


def get_consensus(profile: list) -> str:
    """Get consensus from profile

    Args:
        profile (list): sequence profile

    Returns:
        str: consensus sequence
    """
    lookup_base = {0: "A", 1: "C", 2: "G", 3: "T"}

    transposed_profile = list(zip(*profile))
    consensus = []
    for base_counts in transposed_profile:
        base = base_counts.index(max(base_counts))

        consensus.append(lookup_base[base])
    
    consensus = "".join(consensus)
    return consensus


def process_sequences(sequences: list):
    """Process sequences to print out the results

    Args:
        sequences (list): list of sequences
    """
    transformed_sequences = transform_sequences(sequences)
    profile = calculate_profile(transformed_sequences)
    consensus = get_consensus(profile)

    print(consensus)
    bases = ["A", "C", "G", "T"]
    for i, counts in enumerate(profile):
        counts = [str(count) for count in counts]
        print("{}: {}".format(bases[i], " ".join(counts)))


def load_dataset(file_handle) -> list:
    """Parse a fasta file

    Args:
        file_handle: file handle to fasta file

    Returns:
        list: a list where each element is the sequence
    """
    output = []
    lines = file_handle.readlines()
    name = None
    for line in lines:
        line = line.replace("\n", "")
        if line.startswith(">"):
            if name:
                output.append(sequence)
            name = line[1:]
            sequence = ""
        else:
            sequence += line

    if name:
        output.append(sequence)
    
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Consensus and Profile")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequences = load_dataset(f)
    
    process_sequences(sequences)
