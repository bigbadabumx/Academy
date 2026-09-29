import unittest
from decimal import Decimal

from src.reports import totals_by_region


class ReportTests(unittest.TestCase):
    def test_totals_by_region_use_completed_orders(self) -> None:
        customers = [
            {"customer_id": "C001", "name": "Northwind", "region": "Lisboa"},
            {"customer_id": "C002", "name": "Contoso", "region": "Centro"},
        ]
        orders = [
            {
                "order_id": "O1",
                "customer_id": "C001",
                "status": "completed",
                "amount": "10.00",
            },
            {
                "order_id": "O2",
                "customer_id": "C002",
                "status": "pending",
                "amount": "20.00",
            },
        ]

        result = totals_by_region(customers, orders)

        self.assertEqual(result, {"Lisboa": Decimal("10.00")})


if __name__ == "__main__":
    unittest.main()

