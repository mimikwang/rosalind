"""Rabbits and Recurrence Relations

http://rosalind.info/problems/fib/
"""


def count_rabbits(previous: int, current: int, k: int) -> int:
    """Given the previous month's count and current count, return the next month's count

    Args:
        previous (int): previous month's rabbit pairs
        current (int): current month's rabbit pairs
        k (int): number of rabbit pairs in a litter

    Returns:
        int: next month's count
    """
    count = current + previous*k
    return count


def recursive_count(n: int, k: int) -> int:
    """Recursively count the number of rabbit pairs after n months

    Args:
        n (int): number of months
        k (int): number of rabbit pairs in a litter

    Returns:
        int: number of rabbit pairs after n months
    """
    if n <= 2:
        return 1
    
    previous = 1
    current = 1
    for _ in range(n - 2):
        count = count_rabbits(previous, current, k)
        previous = current
        current = count
    
    return count


def load_dataset(file_handle) -> tuple:
    input_data = file_handle.readline()
    k, n = input_data.split(" ")
    return int(k), int(n)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rabbits and Recurrence Relations")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        k, n = load_dataset(f)
    
    output = recursive_count(k, n)
    print(output)
