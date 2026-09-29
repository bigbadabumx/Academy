"""Small pricing functions used by the exercises."""

from decimal import Decimal


def apply_discount(amount: Decimal, discount_percent: int) -> Decimal:
    """Apply a percentage discount to an amount."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount must be between 0 and 100")

    discount = amount * Decimal(discount_percent) / Decimal("100")
    return amount - discount


def is_valid_order_amount(amount: Decimal) -> bool:
    """Return whether an amount can be used in an order.

    There is a deliberate edge-case bug here for the bugfix exercise.
    """
    return amount >= Decimal("0")

