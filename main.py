from typing import Generator, Any
from itertools import permutations


def permutations_gen(given_list: list[Any]) -> Generator[list[Any], None, None]:
    """
    Generate permutations of the elements in the given list.

    Args:
        given_list (list[Any]): The list whose elements' permutations are to be generated.

    Yields:
        Generator[list[Any], None, None]: A generator object that yields permutations of the given list.

    Returns:
        Generator[list[Any], None, None]: A generator object that yields permutations of the given list.
    """
    for permutation in permutations(given_list):
        yield list(permutation)


def main() -> None:
    """
    Main function to generate and print permutations of a list.
    """
    for i in permutations_gen([1, None, 5, True]):
        print(i)


if __name__ == '__main__':
    main()
