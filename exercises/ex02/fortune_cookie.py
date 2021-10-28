"""Program that outputs one of at least four random, good fortunes."""

<<<<<<< HEAD
<<<<<<< HEAD
__author__ = "730425339"
=======
__author__ = "730243388"
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
=======
__author__ = "ENTER YOUR 9-DIGIT PID HERE"
>>>>>>> 7eeff2db141e2d6eb3717903a147712487fff7e1

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


<<<<<<< HEAD
# Begin your solution here...
<<<<<<< HEAD
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
=======

rand_int: int = randint(0, 3)
print("Your fortune cookie says...")
if (rand_int == 0):
    print("you will get married")
elif (rand_int == 1):
    print("you should take a nap")
elif (rand_int == 2):
    print("you need therapy")
else:
    print("you will meet a new friend tommorow")
print("Now, go spread positive vibes!")
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
=======
# Begin your solution here...
>>>>>>> 7eeff2db141e2d6eb3717903a147712487fff7e1
