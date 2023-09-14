import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("northwind.db")
query = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
'''

top_employees = pd.read_sql_query(query, conn)
top_employees.plot(x="Employee", y="Total", kind="bar", figsize=(10, 5), legend=False)

plt.title("TOP TEN PERFORMANCE EMPLOYEES")
plt.xlabel("Employee")
plt.ylabel("Total")
plt.xticks(rotation=45)
plt.show()
