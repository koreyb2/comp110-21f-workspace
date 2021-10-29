"""Utility functions."""

__author__ = "730425339"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Convert rows of CSV files into a list of dictionaries."""
    table: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        table.append(row)
    file_handle.close()
    return table


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(x: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Table with only first N rows."""
    result: dict[str, list[str]] = {}
    if N >= len(x):
        for column in x:
            result[column] = x[column]
        return result
    for column in x:
        n_values: list[str] = []
        i: int = 0
        while i < N:
            n_values.append(x[column][i])
            i += 1
        result[column] = n_values
    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Table of specified columns."""
    result: dict[str, list[str]] = {}
    i: int = 0
    while i < len(y):
        result[y[i]] = x[y[i]]
        i += 1
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables."""
    result: dict[str, list[str]] = {}
    for key in x:
        result[key] = x[key]
    for k in y:
        result[k] = y[k]
    return result


def count(x: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    i: int = 0
    while i < len(x):
        if x[i] in result:
            result[x[i]] += 1
        else:
            result[x[i]] = 1
        i += 1
    return result

