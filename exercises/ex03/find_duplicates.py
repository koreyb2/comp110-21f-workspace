"""Finding duplicate letters in a word."""

<<<<<<< HEAD
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
=======
__author__ = "123456789"
<<<<<<< HEAD

word: str = input("Enter a word: ")

i: int = 0
duplicate: bool = False
while (i < len(word)):
    j: int = i + 1
    while(j < len(word)):
        if (word[i] == word[j]):
            duplicate = True
        j += 1
    i += 1

print("Found duplicate: " + str(duplicate))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
=======
>>>>>>> 7eeff2db141e2d6eb3717903a147712487fff7e1
