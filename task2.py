# i will continue on project one data set made a seperate file for task 2
import pandas as pd
import matplotlib.pyplot as plt
corrected_data=pd.read_csv(r"E:\uefn downloads\Dataset for Data Analytics.csv")
print(corrected_data.isnull().sum(),"\n")
print(corrected_data["CouponCode"],"\n")
corrected_data["CouponCode"]=corrected_data["CouponCode"].fillna("SAVE10")
print(corrected_data.isnull().sum(),"\n")
#handeled the null values in coupon code
print("---------------------------------\n")
print(corrected_data.duplicated().any(),"\n")
#there is no duplicated data
print("---------------------------------\n")
print(corrected_data.dtypes,"\n")
print(corrected_data["TrackingNumber"],"\n")
corrected_data['Date']=pd.to_datetime(corrected_data["Date"])
print(corrected_data.dtypes,"\n")
#changed the datatype of date to datetime
print("---------------------------------\n")
# i will calculate all the mean median and count for all the numerical data
print("unit price")
print(corrected_data["UnitPrice"].mean())
print(corrected_data["UnitPrice"].median())
print("---------------------------------\n")
print("Quantity")
print(corrected_data["Quantity"].mean())
print(corrected_data["Quantity"].median())
print("---------------------------------\n")
print("ItemsInCart")
print(corrected_data["ItemsInCart"].mean())
print(corrected_data["ItemsInCart"].median())
print("---------------------------------\n")
print("TotalPrice")
print(corrected_data["TotalPrice"].mean())
print(corrected_data["TotalPrice"].median())
#all of their count is 1200
#now the outliers in total price
print("---------------------------------\n")
q1=corrected_data["TotalPrice"].quantile(0.25)
q3=corrected_data["TotalPrice"].quantile(0.75)
iqr=q3-q1

lower_limit = q1-1.5*iqr
upper_limit= q3+1.5*iqr

outliers = corrected_data[ (corrected_data["TotalPrice"] < lower_limit) | (corrected_data["TotalPrice"] > upper_limit)]
print(outliers)
#and i will make trend for the monthly sales and top products sold
monthly_sales = corrected_data.groupby(corrected_data["Date"].dt.to_period("M"))["TotalPrice"].sum()
print(monthly_sales)
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()
print("---------------------------------\n")
top_products = corrected_data.groupby("Product")["TotalPrice"].sum()
print(top_products.sort_values())
plt.title("top_products")
plt.xlabel("products")
plt.ylabel("units sold")
top_products.plot()
plt.show()
# i will make a summary in a documentation
