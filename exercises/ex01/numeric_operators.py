<<<<<<< HEAD
"""Numeric Operators."""

__author__ = 730425339

Left: int = int(input("Left-hand side: "))
Right: int = int(input("Right-hand side: "))
exponent = int(Left) ** int(Right)
print(str(Left) + " ** " + str(Right) + " is " + str(exponent))
division = int(Left) / int(Right)
print(str(Left) + " / " + str(Right) + " is " + str(division))
integer_divison = int(Left) // int(Right)
print(str(Left) + " // " + str(Right) + " is " + str(integer_divison))
remainder = int(Left) % int(Right)
print(str(Left) + " % " + str(Right) + " is " + str(remainder))
=======
"""Demonstrates python numeric operators for two input numbers."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " ** " + string_two + " is " + str(number_one ** number_two))
print(string_one + " / " + string_two + " is " + str(number_one / number_two))
print(string_one + " // " + string_two + " is " + str(number_one // number_two))
print(string_one + " % " + string_two + " is " + str(number_one % number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
