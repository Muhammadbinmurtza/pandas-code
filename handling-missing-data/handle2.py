#fillna()
#fillna(value, inplace=True)

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
# For count of missing values
print(df.isnull().sum())  # Count of missing values in each column
# Fill missing values with a specified value
df['age'].fillna(df['age'].mean(), inplace=True)  # Replace NaN with 0
print(df)

# df['age'].fillna(df['age'].mean(),inplace=True)  # Replace NaN in 'age' with the mean of the column
# df['performance_score'].fillna(df['performance_score'].median())  # Replace NaN in 'performance_score' with the median of the column
# print("----------------------------------------------------------")

# numeric_cols = ['age', 'salary', 'performance_score']
# df[numeric_cols] = df[numeric_cols].astype(float)
# df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
# print(df)  # Replace NaN in numeric columns with their mean