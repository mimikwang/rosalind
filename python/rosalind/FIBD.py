"""Mortal Fibonacci Rabbits

http://rosalind.info/problems/fibd/
"""


def recursive_count(n: int, m: int) -> int:
    """Recursively count the number of rabbit pairs after n months

    Args:
        n (int): number of months
        m (int): lifespan of rabbit in months

    Returns:
        int: number of rabbit pairs after n months
    """
    if n <= 2:
        return 1
    
    tracker = [1, 1]
    for month in range(n - 2):
        current = tracker[month] + tracker[month + 1]
        if month == (m - 2):
            current -= 1
        elif month > (m - 2):
            current -= tracker[-m - 1]
        
        tracker.append(current)
    
    return tracker[-1]


def load_dataset(file_handle) -> tuple:
    input_data = file_handle.readline()
    n, m = input_data.split(" ")
    return int(n), int(m)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Mortal Fibonacci Rabbits")
    parser.add_argument("input_file", help="Path to input dataset")
    args = parser.parse_args()

    with open(args.input_file) as f:
        n, m = load_dataset(f)
    
    output = recursive_count(n, m)
    print(output)
