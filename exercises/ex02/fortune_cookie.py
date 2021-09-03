"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730425339"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune = randint(1, 4)

if fortune == 1:
    print("Your fortune cookie says...")
    print("All your troubles will be resolved soon.")
    print("Now, go spread positive vibes!")
else:
    if fortune == 2:
        print("Your fortune cookie says...")
        print("The adventure of a lifetime is just around the corner!")
        print("Now, go spread positive vibes!")
    else:
        if fortune == 3:
            print("Your fortune cookie says...")
            print("An interesting person will soon cross paths with you.")
            print("Now, go spread positive vibes")
        else:
            if fortune == 4:
                print("Your fortune cookies says...")
                print("Relaxing days are in your future.")
                print("Now, go spread positive vibes!")
            else:
                print("error")