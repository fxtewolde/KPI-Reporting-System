import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

start_date = datetime(2025, 6, 1)
dates = [start_date + timedelta(days=i) for i in range(180)]

regions = [
    "Ontario", 
    "Quebec",
    "British Columbia",
    "Alberta",
    "Atlantic",
]
            ##   Change Regions ***

rows = []
for date in dates:
    for region in regions:
        shipments = np.random.randint(50, 300)

        on_time_pct = np.clip(
            np.random.normal(0.91, 0.05),
            0.6,
            1.0
        )

        avg_cost = np.random.normal(12.5, 2.0)

        delay_cause = np.random.choice(
            ["Weather", "Customs", "Carrier Capacity", "None"],
            p=[0.10, 0.05, 0.10, 0.75]
        )

        rows.append([
            date.strftime("%Y-%m-%d"),
            region,
            shipments,
            round(on_time_pct, 3),
            round(avg_cost, 2),
            delay_cause
        ])

df = pd.DataFrame(
    rows,
    columns=[
        "ship_date",
        "region",
        "shipments",
        "on_time_pct",
        "avg_cost_per_shipment",
        "delay_cause"
    ]
)

print(df.head())
print()
print("Number of rows:", len(df))

conn = sqlite3.connect("logistics.db")

df.to_sql(
    "shipments",
    conn,
    if_exists = "replace",
    index = False
)

conn.close()
print("Database created... in logistics.db")