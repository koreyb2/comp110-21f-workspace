"""Relational Operators."""

__author__ = 730425339

Left: int = int(input("Left-hand side: "))
Right: int = int(input("Right-hand side: "))
Line3 = int(Left) < int(Right)
print(str(Left) + " < " + str(Right) + " is " + str(Line3))
Line4 = int(Left) >= int(Right)
print(str(Left) + " >= " + str(Right) + " is " + str(Line4))
Line5 = int(Left) == int(Right)
print(str(Left) + " == " + str(Right) + " is " + str(Line5))
Line6 = int(Left) != int(Right)
print(str(Left) + " != " + str(Right) + " is " + str(Line6))
