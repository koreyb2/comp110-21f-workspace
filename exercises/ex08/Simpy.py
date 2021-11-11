"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730425339"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        self.values = values

    def __str__(self) -> str:
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int) -> None:
        while len(self.values) < y:
            self.values.append(x)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
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
        return sum(self.values)

    def __add__(self, lhs: Union[Simpy, float])