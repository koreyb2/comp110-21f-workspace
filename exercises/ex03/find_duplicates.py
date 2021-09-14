"""Finding duplicate letters in a word."""

__author__ = "730425339"

user_word: str = str(input("Enter a word: "))
i: int = 0
duplicate: str = "False"

while i < len(user_word):
    char = user_word[i]
    j: int = i + 1
    while j < len(user_word):
        if char == user_word[j]:
            duplicate = "True"
        j += 1
    i += 1
duplicate: str = duplicate
print("Found duplicate: " + duplicate)