import sqlite3
import pandas as pd 

conn = sqlite3.connect("logistics.db")

q1 = """
SELECT
    region,
    ROUND(AVG(on_time_pct) * 100, 1) AS avg_on_time_pct
FROM shipments
GROUP BY region
ORDER BY avg_on_time_pct DESC;
"""

kpi1 = pd.read_sql(q1, conn)

print("KPI 1: On-Time Delivery by Region")
print("Which regions have the best/worst delivery performance?")
print(kpi1)

q2 = """
SELECT
    strftime('%Y-%m', ship_date) AS month,
    ROUND(AVG(avg_cost_per_shipment), 2) AS avg_cost
FROM shipments
GROUP BY month
ORDER BY month;
"""

kpi2 = pd.read_sql(q2, conn)

print()
print("KPI 2: Average Cost per Shipment by Month")
print("Is our cost per shipment increasing or decreasing over time?")
print(kpi2)

q3 = """
SELECT
    delay_cause,
    COUNT(*) AS occurrences
FROM shipments
WHERE delay_cause != 'None'
GROUP BY delay_cause
ORDER BY occurrences DESC;
"""

kpi3 = pd.read_sql(q3, conn)

print()
print("KPI 3: Delay Cause Breakdown")
print("Why are the shipments with the most occurences being delayed?")
print(kpi3)

##Excel KPI Report
with pd.ExcelWriter(
    "Weekly_KPI_Report.xlsx",
    engine = "openpyxl"
) as writer:

    kpi1.to_excel(
        writer,
        sheet_name = "On-time by Region",
        index = False
    )

    kpi2.to_excel(
        writer,
        sheet_name="Cost Trend",
        index=False
    )

    kpi3.to_excel(
        writer,
        sheet_name="Delay Causes",
        index=False
    )

print()
print("Weekly KPI report generated.")


conn.close()