"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730425339"


def test_only_evens_empty() -> None:
    """Only evens function when the list is empty."""
    assert only_evens([]) == []


def test_only_evens_odds() -> None:
    """Only evens function when the list is only odds."""
    assert only_evens([1, 3, 5, 7, 9, 11]) == []


def test_only_evens_mixed() -> None:
    """Only evens function when the list is a mix of odds and evens."""
    assert only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 4, 6, 8]


def test_sub_start() -> None:
    """Sub function when starting index is greater than the length."""
    assert sub([1, 2, 3, 4], 5, 6) == []


def test_sub_within() -> None:
    """Sub function within a list."""
    assert sub([4, 6, 8, 10, 12], 1, 3) == [6, 8]


def test_sub_entire() -> None:
    """Sub function over entire list except last value."""
    assert sub([1, 2, 3, 4, 5, 6], 0, 5) == [1, 2, 3, 4, 5]


def test_concat_empty() -> None:
    """Concat with no arguments."""
    assert concat([], []) == []


def test_concat_one() -> None:
    """Concat with only arguments in the second list."""
    assert concat([], [3, 6, 9, 12, 15]) == [3, 6, 9, 12, 15]


def test_concat_combine() -> None:
    """Concat combining two equal length lists."""
    assert concat([1, 2, 3, 4], [5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]