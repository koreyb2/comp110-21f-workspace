"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730425339"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the list of floats."""
        self.values = values

    def __str__(self) -> str:
        """Convert object to a string."""
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        """Create a list of one value repeated a certain number of times."""
        self.values = []
        while len(self.values) < y:
            self.values.append(x)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Create a list of values between two points in increments."""
        assert step != 0.0
        self.values = []
        if stop < 0.0:
            while start > stop:
                self.values.append(start)
                start += step
        else:
            while start < stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Sum all values."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add values in a Simpy object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise a list of floats to a power."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test whether one object is equal to another."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test whether one item is greater than another."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Add subscription notation for Simpy."""
        if isinstance(rhs, int):
            result_float: float = 0.0
            i: int = 0
            while i < len(self.values):
                if i == rhs:
                    result_float = self.values[i]
                i += 1
            return result_float
        else:
            result_Simpy: Simpy = Simpy([])
            x: int = 0
            while x < len(rhs):
                if rhs[x]:
                    result_Simpy.values.append(self.values[x])
                x += 1
            return result_Simpy