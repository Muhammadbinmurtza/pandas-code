import pandas as pd
data = {
    "name": ["Alice", 'muhammad', "Charlie", "David", "Eve", "Frank"],
    "age": [25, None, 35, 40, 45, 50],
    "city": ["New York", 'nivada', "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "salary": [70000, None, 90000, 100000, 110000, 120000],
    "performance_score": [85, None, 95, 80, 75, 88],
}
df = pd.DataFrame(data)
print(df)

#methods : linear, polynomial, spline,time
# Interpolating missing values
df.interpolate(method="linear", inplace=True, axis=0)  # Interpolate missing values, axis= 0 for rows, axis=1 for columns