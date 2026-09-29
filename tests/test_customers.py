import unittest

from src.customers import customers_by_region, find_customer


class CustomerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.customers = [
            {"customer_id": "C001", "name": "Northwind", "region": "Lisboa"},
            {"customer_id": "C002", "name": "Contoso", "region": "Centro"},
        ]

    def test_find_existing_customer(self) -> None:
        customer = find_customer(self.customers, "C002")
        self.assertIsNotNone(customer)
        self.assertEqual(customer["name"], "Contoso")

    def test_missing_customer_returns_none(self) -> None:
        self.assertIsNone(find_customer(self.customers, "C999"))

    def test_region_filter_ignores_case(self) -> None:
        result = customers_by_region(self.customers, "centro")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["customer_id"], "C002")


if __name__ == "__main__":
    unittest.main()

