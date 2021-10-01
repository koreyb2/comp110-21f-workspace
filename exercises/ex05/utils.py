"""List utility functions part 2."""

__author__ = "730425339"

# Define your functions below


def only_evens(x: list[int]) -> list[int]:
    """Return only even numbers from a list."""
    y: list[int] = []
    i: int = 0
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
        i += 1
    return y


def sub(a: list[int], start: int, end: int) -> list[int]:
    """Interval from a given list."""
    subset: list[int] = []
    if len(a) == 0 or start > len(a) or end <= 0:
        return subset
    if start < 0:
        start = start - start
    if end > len(a):
        difference: int = end - len(a)
        end = end - difference
    while start < end:
        subset.append(a[start])
        start = start + 1
    return subset


def concat(first: list[int], second: list[int]) -> list[int]:
    """Combining two lists."""
    i: int = 0
    combined: list[int] = []
    while i < len(first):
        combined.append(first[i])
        i += 1
    i = 0
    while i < len(second):
        combined.append(second[i])
        i += 1
    return combined
