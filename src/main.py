"""Command-line entry point."""

from pathlib import Path

from src.customers import load_customers
from src.orders import load_orders
from src.reports import build_report


def main() -> None:
    # Local Computer
    project_root = Path(__file__).resolve().parents[1]
    # Databricks
    # project_root = Path.cwd().parent
    customers = load_customers(project_root / "data" / "customers.csv")
    orders = load_orders(project_root / "data" / "orders.csv")
    print(build_report(customers, orders))


if __name__ == "__main__":
    main()

