"""Repeating a beat in a loop."""

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