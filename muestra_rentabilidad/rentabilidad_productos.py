import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("northwind.db")
query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    From OrderDetails od
    Join Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

top_products = pd.read_sql_query(query, conn)
top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10, 5), legend=False)
plt.title("TOP TEN PRODUCTS SOLD")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.xticks(rotation=90)
plt.show()
