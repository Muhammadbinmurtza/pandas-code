import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "age": [25, 31, 35, 40, 45, 50],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "salary": [70000, 80000, 90000, 100000, 110000, 120000],
    "performance_score": [85, 90, 95, 80, 75, 88],
}

df = pd.DataFrame(data)

high_salary = df[df["salary"] > 90000]
print("Employees with salary greater than 90000:")
print(high_salary)

# multiple conditions
high_perf_ny = df[(df["performance_score"] > 90) & (df["salary"] > 80000)]
print("\nEmployees with performance score greater than 90 and salary greater than 80000:")
print(high_perf_ny)

#using or condition
age_or_city = df[(df["age"] < 30) | (df["city"] == "Chicago")]
print("\nEmployees who are either younger than 30 or live in Chicago:")
print(age_or_city)
