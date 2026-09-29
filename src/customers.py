"""Customer loading and lookup functions."""

from __future__ import annotations

import csv
from pathlib import Path


def load_customers(path: str | Path) -> list[dict[str, str]]:
    """Load customer rows from a CSV file."""
    with Path(path).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def find_customer(
    customers: list[dict[str, str]], customer_id: str
) -> dict[str, str] | None:
    """Return one customer or None when the identifier does not exist."""
    for customer in customers:
        if customer["customer_id"] == customer_id:
            return customer
    return None


def customers_by_region(
    customers: list[dict[str, str]], region: str
) -> list[dict[str, str]]:
    """Return customers from a region, ignoring letter case."""
    expected = region.casefold()
    return [
        customer
        for customer in customers
        if customer["region"].casefold() == expected
    ]

