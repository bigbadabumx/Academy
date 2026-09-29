import unittest
from decimal import Decimal

from src.pricing import apply_discount, is_valid_order_amount


class PricingTests(unittest.TestCase):
    def test_apply_discount(self) -> None:
        result = apply_discount(Decimal("100"), 15)
        self.assertEqual(result, Decimal("85"))

    def test_reject_invalid_discount(self) -> None:
        with self.assertRaises(ValueError):
            apply_discount(Decimal("100"), 120)

    def test_positive_order_amount_is_valid(self) -> None:
        self.assertTrue(is_valid_order_amount(Decimal("0.01")))

    def test_negative_order_amount_is_invalid(self) -> None:
        self.assertFalse(is_valid_order_amount(Decimal("-1")))


if __name__ == "__main__":
    unittest.main()

