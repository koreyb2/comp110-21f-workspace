"""Repeating a beat in a loop."""

__author__ = "730425339"


# Begin your solution here...
beat_choice: str = input("What beat do you want to repeat? ")

beat_times: int = int(input("How many times do you want to repeat it? "))

i: int = 0

while i < beat_times:
    print(beat_choice)
    i = i + 1

while beat_times <= 0:
    print("No beat...")
    beat_times = (beat_times - beat_times) + 1
