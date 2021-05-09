"""Finding a Shared Motif

http://rosalind.info/problems/lcsm/
"""


def chop_sequence(sequence: str) -> set:
    """Chop up a sequence and update the counter

    Args:
        counter (dict): counter to be updated
        sequence (str): sequence to be chopped up

    Return:
        set: the set of motifs
    """
    motifs = set()
    for length in range(2, len(sequence) + 1):
        for base_index in range(len(sequence) - length + 1):
            motif = sequence[base_index:base_index+length]
            motifs.add(motif)
    
    return motifs


def find_shared_motifs(sequences: list) -> set:
    """Given a list of sequences, find all the shared motifs

    Args:
        sequences (list): list of sequences

    Returns:
        set: shared motifs
    """
    shared_motifs = None
    for sequence in sequences:
        motifs = chop_sequence(sequence)
        if not shared_motifs:
            shared_motifs = motifs
        else:
            shared_motifs = shared_motifs & motifs
    
    return shared_motifs


def get_longest_motif(motifs: set) -> str:
    """Return the longest motif in a set

    Args:
        motifs (set): motifs

    Returns:
        str: the longest motif
    """
    motifs = [motif for  motif in motifs]
    motifs = sorted(motifs)
    motifs = sorted(motifs, key=lambda x: len(x), reverse=True)
    return motifs[0]


def find_longest_shared_motif(sequences: list) -> str:
    """Find the longest shared motif

    Args:
        sequences (list): list of sequences

    Returns:
        str: the longest motif
    """
    shared_motifs = find_shared_motifs(sequences)
    longest_motif = get_longest_motif(shared_motifs)
    return longest_motif


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

    parser = argparse.ArgumentParser(description="Finding a Shared Motif")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequences = load_dataset(f)
    
    output = find_longest_shared_motif(sequences)
    print(output)
