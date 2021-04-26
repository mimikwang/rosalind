"""Mendel's First Law

http://rosalind.info/problems/iprb/
"""
import itertools as it


"""
Define the probabilities for each combination as a dict.  "AA" denotes homozygous dominant, "Aa" denotes
heterozygous, and "aa" denotes homozygous recessive.  The probabilities correspond to the chance of having at least
one dominant allele.
"""
PROBABILITIES = {
    ("AA", "AA"): 1,
    ("AA", "aa"): 1,
    ("AA", "Aa"): 1,
    ("Aa", "AA"): 1,
    ("Aa", "aa"): 0.5,
    ("Aa", "Aa"): 0.75,
    ("aa", "AA"): 1,
    ("aa", "aa"): 0,
    ("aa", "Aa"): 0.5
}


def calculate_probability(k: int, m: int, n: int) -> float:
    """Calculate the probability of of creating an offspring with a dominant allele

    Args:
        k (int): the number of homozygeous dominant
        m (int): the number of heterozeygous
        n (int): the number of homozygeous recessive

    Returns:
        float: the probability of creating an offspring with a dominant allele
    """
    population = ["AA" for _ in range(k)] + ["Aa" for _ in range(m)] + ["aa" for _ in range(n)]
    pairings = it.combinations(population, 2)
    probabilities = [PROBABILITIES[pairing] for pairing in pairings]
    output = sum(probabilities) / len(probabilities)

    return output


def load_dataset(file_handle) -> tuple:
    input_data = file_handle.readline()
    k, m, n = input_data.split(" ")
    return int(k), int(m), int(n)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Mendel's First Law")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        k, m, n = load_dataset(f)
    
    output = calculate_probability(k, m, n)
    print(output)
