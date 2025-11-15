#adding columns 
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "age": [25, 31, 35, 40, 45, 50],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "salary": [70000, 80000, 90000, 100000, 110000, 120000],
    "performance_score": [85, 90, 95, 80, 75, 88],
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df["salary"] * 0.1
print(df)

#using insert method

df.insert(2, "Department", ["HR", "Finance", "IT", "Marketing", "Sales", "Operations"])
print(df)
