"""Report creation functions."""

from __future__ import annotations

from collections import defaultdict
from decimal import Decimal

from src.config import COMPANY_NAME, CURRENCY, REPORT_TITLE
from src.customers import find_customer
from src.orders import orders_with_status, total_amount


def totals_by_region(
    customers: list[dict[str, str]], orders: list[dict[str, str]]
) -> dict[str, Decimal]:
    """Calculate completed sales totals grouped by customer region."""
    result: dict[str, Decimal] = defaultdict(lambda: Decimal("0"))

    for order in orders_with_status(orders, "completed"):
        customer = find_customer(customers, order["customer_id"])
        region = customer["region"] if customer else "Unknown"
        result[region] += Decimal(order["amount"])

    return dict(sorted(result.items()))


def build_report(
    customers: list[dict[str, str]], orders: list[dict[str, str]]
) -> str:
    """Build the command-line sales report."""
    completed = orders_with_status(orders, "completed")
    lines = [
        COMPANY_NAME,
        REPORT_TITLE,
        "=" * len(REPORT_TITLE),
        f"Completed orders: {len(completed)}",
        f"Completed total: {CURRENCY} {total_amount(completed):.2f}",
        "Sales by region:",
    ]

    for region, amount in totals_by_region(customers, orders).items():
        lines.append(f"  {region}: {CURRENCY} {amount:.2f}")

    return "\n".join(lines)

