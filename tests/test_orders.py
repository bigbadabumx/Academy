import unittest
from decimal import Decimal

from src.orders import orders_for_customer, orders_with_status, total_amount


class OrderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.orders = [
            {
                "order_id": "O1",
                "customer_id": "C001",
                "status": "completed",
                "amount": "10.50",
            },
            {
                "order_id": "O2",
                "customer_id": "C001",
                "status": "pending",
                "amount": "7.25",
            },
            {
                "order_id": "O3",
                "customer_id": "C002",
                "status": "completed",
                "amount": "5.00",
            },
        ]

    def test_filter_by_status(self) -> None:
        result = orders_with_status(self.orders, "COMPLETED")
        self.assertEqual(len(result), 2)

    def test_total_amount(self) -> None:
        self.assertEqual(total_amount(self.orders), Decimal("22.75"))

    def test_orders_for_customer(self) -> None:
        result = orders_for_customer(self.orders, "C001")
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()

