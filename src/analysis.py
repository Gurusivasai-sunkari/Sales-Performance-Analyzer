import numpy as np

def analyze_sales(sales, months):

    print("\n===== SALES REPORT =====\n")

    print("Total Sales:", np.sum(sales), "$")
    print("Average Sales:", round(np.mean(sales), 2), "$")
    print("Highest Sales:", np.max(sales), "$")
    print("Lowest Sales:", np.min(sales), "$")

    print("Best Month:", months[np.argmax(sales)])
    print("Worst Month:", months[np.argmin(sales)])

    above_avg = months[sales > np.mean(sales)]
    print("\nAbove Average Months:", above_avg)

    q1 = np.sum(sales[:3])
    q2 = np.sum(sales[3:6])
    q3 = np.sum(sales[6:9])
    q4 = np.sum(sales[9:12])

    print("\nQuarterly Sales")
    print("Q1:", q1, "$")
    print("Q2:", q2, "$")
    print("Q3:", q3, "$")
    print("Q4:", q4, "$")

    growth = ((sales[-1] - sales[0]) / sales[0]) * 100

    print("\nGrowth Percentage:", round(growth, 2), "%")

    if sales[-1] > sales[0]:
        print("Business Trend: Growing 📈")
    elif sales[-1] < sales[0]:
        print("Business Trend: Declining 📉")
    else:
        print("Business Trend: Stable")

    top3 = np.argsort(sales)[-3:]

    print("\nTop 3 Months:")

    for i in reversed(top3):
        print(months[i], ":", sales[i], "$")
