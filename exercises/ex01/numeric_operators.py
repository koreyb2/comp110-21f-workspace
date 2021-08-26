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
