# df['column'].mean()
#df['column'].min()
#df['column'].max()

import pandas as pd

data = {
    "Name" : ["muhammad","ahmad", "umar"],
    "age" : [28,34,22],
    "salary" : [10000,20000,30000]
    }

df = pd.DataFrame(data)
print("data before sorting")
print(df)

avg_salary = df['salary'].mean()
print(avg_salary)

df.to_csv("data_csv.csv",index=True)