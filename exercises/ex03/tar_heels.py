"""An exercise in remainders and boolean logic."""

__author__ = "730425339"


# Begin your solution here...
user_input: int = int(input("Enter an int: "))

if user_input % 2 == 0:
    if user_input % 7 == 0:
        print("TAR HEELS")
    else: 
        print("TAR")

if user_input % 7 == 0:
    if user_input % 2 != 0:
        print("HEELS")

if user_input % 2 != 0:
    if user_input % 7 != 0:
        print("CAROLINA")
