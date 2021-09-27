"""List utility functions."""

__author__ = "730425339"


# TODO: Implement your functions here.


def all(x: list[int], y: int) -> bool:
    """All."""
    i: int = 0
    counter: int = 0
    while i < len(x):
        if x[i] == y:
            counter += 1
        i += 1
    if counter == len(x):
        return True
    return False


def is_equal(x: list[int], y: list[int]) -> bool:
    """Equality."""
    counter: int = 0
    i: int = 0
    if len(x) != len(y):
        return False
    while i < len(x) or i < len(y):
        if x[i] == y[i]:
            counter += 1
        else:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Return max value."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_value: int = input[0]
    i: int = 1
    while i < len(input):
        if input[i] > max_value:
            max_value = input[i]
        i += 1
    return max_value