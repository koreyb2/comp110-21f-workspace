"""Drawing forests in a loop."""

__author__ = "730425339"

# The string constant for the pine tree emoji
<<<<<<< HEAD
TREE: str = '\U0001F332'
<<<<<<< HEAD
Tree: str = '\U0001F332'
depth: int = int(input("Depth: "))
i: int = 0

while i < depth:
    i = i + 1
    print(TREE)
    TREE = TREE + Tree
=======

depth: int = int(input("Depth: "))

i: int = 0
duplicate: bool = False
while (i < depth):
    j: int = 0
    tree: str = ""
    while(j < i + 1):
        tree += TREE
        j += 1
    print(tree)
    i += 1
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
=======
TREE: str = '\U0001F332'
>>>>>>> 7eeff2db141e2d6eb3717903a147712487fff7e1
