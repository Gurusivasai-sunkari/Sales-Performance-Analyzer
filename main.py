import numpy as np
from src.analysis import analyze_sales

months = np.array([
    "Jan", "Feb", "Mar", "Apr",
    "May", "Jun", "Jul", "Aug",
    "Sep", "Oct", "Nov", "Dec"
])

sales = []

print("Enter monthly sales in $:")

for month in months:
    value = float(input(f"{month}: "))
    sales.append(value)

sales = np.array(sales)

analyze_sales(sales, months)
