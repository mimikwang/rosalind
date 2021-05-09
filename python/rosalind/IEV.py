"""Calculating Expected Offspring

http://rosalind.info/problems/iev/
"""


"""
Define the probabilities for the offspring to display the dominant phenotype
"""
PROBABILITIES = (
    1,    # AA-AA
    1,    # AA-Aa
    1,    # AA-aa
    0.75, # Aa-Aa
    0.5,  # Aa-aa
    0,    # aa-aa
)


def expected_offsprings(couples: list) -> float:
    """Calculate the expected number of offsprings with the dominant phenotype

    Calculate the expected number of offsprings with the dominant phenotype given a list of 6 integers corresponding
    to the probabilities defined in PROBABILITIES.  It's assumed that each couple produces 2 offsprings.

    Args:
        couples (list): A list of 6 integers corresponding to the couples defined in PROBABILITIES

    Returns:
        float: the expected number of offsprings with the dmoinant phenotype
    """
    expected = 0
    for couple, probability in zip(couples, PROBABILITIES):
        expected += couple * probability
    
    return 2 * expected


def load_dataset(file_handle) -> list:
    input_data = file_handle.readline()
    input_data = input_data.split(" ")
    input_data = [int(x) for x in input_data]

    return input_data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Calculating Expected Offsprings")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        couples = load_dataset(f)
    
    output = expected_offsprings(couples)
    print(output)
