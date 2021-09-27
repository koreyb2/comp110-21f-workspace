"""List utility functions."""

__author__ = "730425339"


# TODO: Implement your functions here.
i: int = 0
counter: int = 0


def main() -> None:
    """Main."""
    print(all([1, 1, 1], 1))


def all(x: list[int], y: int) -> bool:
    """All."""
    global counter
    global i
    while i < len(x):
        if x[i] == y:
            counter += 1
        i += 1
    if counter == len(x):
        return True
    return False


if __name__ == "__main__":
    main()