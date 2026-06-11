Task 2 — Exploratory Data Analysis & Visualization

Extends Task 1 by performing statistical analysis, outlier detection, and visual trend analysis on the same e-commerce dataset using pandas and matplotlib.

Requirements


Python 3.x
pandas
matplotlib


Install dependencies:

bashpip install pandas matplotlib

Usage


Update the file path in the script to point to your local CSV file:


pythoncorrected_data = pd.read_csv("your/path/to/Dataset for Data Analytics.csv")


Run the script:


bashpython task2.py

What the Script Does

StepDescriptionData cleaningRepeats null handling and datetime conversion from Task 1Descriptive statsCalculates mean & median for UnitPrice, Quantity, ItemsInCart, TotalPriceOutlier detectionUses IQR method to identify outliers in TotalPriceMonthly sales trendGroups sales by month and plots a line chartTop productsGroups and sorts total revenue by product and plots a line chart

Outputs


Monthly Sales Trend — line chart showing total sales per month
Top Products — line chart showing total revenue per product


Dataset

Expected CSV with columns: CouponCode, TrackingNumber, Date, UnitPrice, Quantity, ItemsInCart, TotalPrice, Product. Total records: 1200 rows.
