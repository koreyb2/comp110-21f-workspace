"""Drawing forests in a loop."""

__author__ = "730425339"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
Tree: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0

while i < depth:
    i = i + 1
    print(TREE)
    TREE = TREE + Tree
