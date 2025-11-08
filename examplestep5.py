import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "age": [25, 31, 35, 40, 45, 50],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "salary": [70000, 80000, 90000, 100000, 110000, 120000],
    "performance_score": [85, 90, 95, 80, 75, 88],
}

df = pd.DataFrame(data)

#display the data frame
print("sample data")
print(df)

print("names single column")
print(df["name"])

# selcting multiple columns
print("\nselecting multiple columns")
print(df[["name", "age"]])

