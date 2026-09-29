"""Order loading, filtering and aggregation functions."""

from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path


def load_orders(path: str | Path) -> list[dict[str, str]]:
    """Load order rows from a CSV file."""
    with Path(path).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def orders_with_status(
    orders: list[dict[str, str]], status: str
) -> list[dict[str, str]]:
    """Return orders with the requested status."""
    expected = status.casefold()
    return [order for order in orders if order["status"].casefold() == expected]


def total_amount(orders: list[dict[str, str]]) -> Decimal:
    """Return the total amount for a list of orders."""
    return sum((Decimal(order["amount"]) for order in orders), Decimal("0"))


def orders_for_customer(
    orders: list[dict[str, str]], customer_id: str
) -> list[dict[str, str]]:
    """Return all orders belonging to one customer."""
    return [order for order in orders if order["customer_id"] == customer_id]

