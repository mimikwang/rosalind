"""Computing GC Content

http://rosalind.info/problems/gc/
"""


def count_gc(sequence: str) -> float:
    """Count the GC content of a given sequence

    Args:
        sequence (str): input sequence

    Returns:
        float: GC content in percentage
    """
    count = 0
    total = 0
    for base in sequence:
        if base == "G" or base == "C":
            count += 1
        total += 1
    
    gc = 100 * (count / total)
    return gc


def get_max_gc(sequences: list) -> tuple:
    """Given a list of sequences, return the sequence name and GC content of the one with the largest GC content

    Args:
        sequences (list): list of tuples where the first element is the sequence name and the second is the sequence

    Returns:
        tuple: sequence name, gc content
    """
    gc_list = []
    for name, sequence in sequences:
        gc = count_gc(sequence)
        gc_list.append((name, gc))
    
    gc_list.sort(key=lambda x: x[1], reverse=True)

    return gc_list[0]


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

    parser = argparse.ArgumentParser(description="Computing GC Content")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        sequences = load_dataset(f)
    
    output = get_max_gc(sequences)
    print(output)
