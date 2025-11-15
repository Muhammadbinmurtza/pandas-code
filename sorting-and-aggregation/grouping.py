import pandas as pd

data = {
    "Name" : ["muhammad","ahmad", "umar","zohaib","who"],
    "age" : [28,34,22,34,28],
    "salary" : [50000,60000,45000,52000,48000]
    }

df = pd.DataFrame(data)

grouped = df.groupby("age")["salary"].sum()
print(grouped)

grouped2 = df.groupby("Name")["age"].sum()
print(grouped2)

