
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def write_csv(filename, rows):
    if not rows:
        return

    with (OUTPUT_DIR / filename).open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


customers = [
    {
        "customer_id": i,
        "customer_name": f"Customer {i:03d}",
        "email": f"customer{i:03d}@example.com",
        "city": ["Manila", "Imus", "Cebu", "Davao"][i % 4],
        "created_date": (date(2025, 1, 1) + timedelta(days=i * 3)).isoformat(),
    }
    for i in range(1, 21)
]

products = [
    {
        "product_id": i,
        "product_name": name,
        "category": category,
        "unit_price": price,
    }
    for i, (name, category, price) in enumerate(
        [
            ("Laptop", "Electronics", 45000),
            ("Mouse", "Accessories", 650),
            ("Keyboard", "Accessories", 1200),
            ("Monitor", "Electronics", 9800),
            ("Headphones", "Accessories", 2100),
            ("Desk", "Furniture", 5500),
            ("Chair", "Furniture", 3200),
            ("Phone", "Electronics", 28000),
            ("Webcam", "Accessories", 1800),
            ("Printer", "Electronics", 7200),
            ("Tablet", "Electronics", 16000),
            ("USB Drive", "Accessories", 450),
        ],
        start=1,
    )
]

stores = [
    {"store_id": 1, "store_name": "Manila Central", "city": "Manila"},
    {"store_id": 2, "store_name": "Imus Branch", "city": "Imus"},
    {"store_id": 3, "store_name": "Cebu Branch", "city": "Cebu"},
    {"store_id": 4, "store_name": "Davao Branch", "city": "Davao"},
    {"store_id": 5, "store_name": "Quezon City Branch", "city": "Quezon City"},
]

sales = []
start_date = date(2026, 1, 1)

for sale_id in range(1, 101):
    product = random.choice(products)
    quantity = random.randint(1, 4)

    sales.append(
        {
            "sale_id": sale_id,
            "customer_id": random.randint(1, 20),
            "product_id": product["product_id"],
            "store_id": random.randint(1, 5),
            "quantity": quantity,
            "unit_price": product["unit_price"],
            "sale_date": (
                start_date + timedelta(days=random.randint(0, 89))
            ).isoformat(),
        }
    )

write_csv("customers.csv", customers)
write_csv("products.csv", products)
write_csv("stores.csv", stores)
write_csv("sales.csv", sales)

print(f"Sample data created in: {OUTPUT_DIR}")
for filename in ["customers.csv", "products.csv", "stores.csv", "sales.csv"]:
    print(f"{filename}: {(OUTPUT_DIR / filename).stat().st_size:,} bytes")
