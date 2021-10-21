"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730425339"


def test_invert_one() -> None:
    """Invert a dictionary with one item."""
    assert invert({"a": "Carolina"}) == {"Carolina": "a"}


def test_invert_full_dict() -> None:
    """Invert a dictionary."""
    assert invert({"a": "b", "c": "d", "e": "f"}) == {"b": "a", "d": "c", "f": "e"}


def test_invert_dict_numbers() -> None:
    """Dictionary with numbers as strings."""
    assert invert({"a": "2", "b": "1", "c": "3"}) == {"2": "a", "1": "b", "3": "c"}


def test_favorite_color_one() -> None:
    """Return only color."""
    assert favorite_color({"a": "blue"}) == "blue"


def test_favorite_color_tie() -> None:
    """A color is tied for the favorite."""
    assert favorite_color({"a": "blue", "b": "blue", "c": "red", "d": "red"}) == "blue"


def test_favorite_color_full() -> None:
    """Return favorite color from full dict."""
    assert favorite_color({"a": "blue", "b": "red", "c": "green", "d": "green"}) == "green"


def test_count_empty() -> None:
    """Count an empty list."""
    assert count([]) == {}


def test_count_one() -> None:
    """List with one of each value."""
    assert count(["a", "b", "c", "d"]) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_count_multiple() -> None:
    """Multiple of some values."""
    assert count(["a", "b", "a", "b"]) == {"a": 2, "b": 2}