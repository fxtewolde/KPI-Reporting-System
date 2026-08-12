import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("logistics.db")

query = """
SELECT
    strftime('%Y-%m', ship_date) AS month,
    ROUND(AVG(avg_cost_per_shipment), 2) AS avg_cost
FROM shipments
GROUP BY month
ORDER BY month;
"""

monthly = pd.read_sql(query, conn)

conn.close()

plt.figure(figsize=(8, 4))

plt.plot(
    monthly["month"],
    monthly["avg_cost"],
    marker="o"
)

plt.title("Average Cost per Shipment by Month")
plt.xlabel("Month")
plt.ylabel("Average Cost ($)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("cost_trend_chart.png")

plt.show()