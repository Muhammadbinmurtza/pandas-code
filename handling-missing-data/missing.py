
import pandas as pd
data = {
    "name": ["Alice", None, "Charlie", "David", "Eve", "Frank"],
    "age": [25, None, 35, 40, 45, 50],
    "city": ["New York", None, "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "salary": [70000, None, 90000, 100000, 110000, 120000],
    "performance_score": [85, None, 95, 80, 75, 88],
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())  # Check for missing values

#for count of missing values
print(df.isnull().sum())  # Count of missing values in each column