"""Practice with dictionaries."""

__author__ = "730425339"

# Define your functions below


def invert(x: dict[str, str]) -> dict[str, str]:
    """Invert a given dictionary."""
    y = dict([(b, a) for a, b in x.items()])
    if len(y) < len(x):
        raise KeyError("Duplicate keys found in inverted dictionary.")
    return y


print(invert({"e": "a", "y": "b", "z": "c"}))


def favorite_color(x: dict[str, str]) -> str:
    """Return the most mentioned color from a dictionary."""
    favorite: str = ""
    totals: dict[str, int] = {}
    colors: list[str] = []
    for a in x:
        colors.append(x[a])
    i: int = 0
    while i < len(colors):
        if colors[i] in totals:
            totals[colors[i]] += 1
        else:
            totals[colors[i]] = 1
        i += 1
    print(totals)
    return favorite


print(favorite_color({"a": "green", "b": "blue", "c": "blue"}))


def count(x: list[str]) -> dict[str, int]:
    """Count the frequency of items in a list."""
    a: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in a:
            a[x[i]] += 1
        else:
            a[x[i]] = 1
        i += 1
    return a


print(count(["a", "b", "c", "a"]))