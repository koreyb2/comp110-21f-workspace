"""Examples of functions imported elsehwhere."""


THE_ANSWER: int = 42


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


print(f"helpers.py: {__name__}")