"""Relational Operators."""

__author__ = 730425339

Left: int = int(input("Left-hand side: "))
Right: int = int(input("Right-hand side: "))
less_than = int(Left) < int(Right)
print(str(Left) + " < " + str(Right) + " is " + str(less_than))
greater_equal = int(Left) >= int(Right)
print(str(Left) + " >= " + str(Right) + " is " + str(greater_equal))
equal_to = int(Left) == int(Right)
print(str(Left) + " == " + str(Right) + " is " + str(equal_to))
not_equal = int(Left) != int(Right)
print(str(Left) + " != " + str(Right) + " is " + str(not_equal))
