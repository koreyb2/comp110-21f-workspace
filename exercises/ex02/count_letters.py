"""Counting letters in a string."""

<<<<<<< HEAD
<<<<<<< HEAD
__author__ = "730425339"


# Begin your solution here...
letter_search: str = str(input("What letter do you want to search for?: "))

word_enter: str = str(input("Enter a word: "))

counter: int = 0
i: int = 0

while i < len(word_enter):
    if word_enter[i] == letter_search:
        counter = counter + 1
        i = i + 1
    else:
        i = i + 1

print("Count: " + str(counter))
=======
__author__ = "730243388"


# Begin your solution here...

letter: str = input("What letter do you want to seach for? ")
word: str = input("Enter a word ")
count: int = 0
i: int = 0
while (i < len(word)):
    if word[i] == letter:
        count += 1
    i += 1
print("Count: " + str(count))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
=======
__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
>>>>>>> 7eeff2db141e2d6eb3717903a147712487fff7e1
