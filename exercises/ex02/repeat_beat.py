"""Repeating a beat in a loop."""

<<<<<<< HEAD
<<<<<<< HEAD
__author__ = "730425339"


# Begin your solution here...
beat_choice: str = input("What beat do you want to repeat? ")

beat_times: int = int(input("How many times do you want to repeat it? "))

i: int = 1
beat_number: str = beat_choice

while i == beat_times:
    beat_number = beat_number
    i = i + 1

while i < beat_times:
    i = i + 1
    beat_number = beat_number + " " + beat_choice

while beat_times <= 0:
    print("No beat...")
    beat_times = (beat_times - beat_times) + 1

while i > 1:
    print(beat_number)
    i = i - i
=======
__author__ = "730243388"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
i: int = 0
if (number < 1):
    print("No beat...")
else:
    print_beat = beat
    while (i < number - 1):
        print_beat += "" + beat

    print(print_beat)
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
=======
__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
>>>>>>> 7eeff2db141e2d6eb3717903a147712487fff7e1
