import pandas as pd

data  = {
    "name" : ["Alice", "Bob", "Charlie"],
    "age" : [25, 30, 35],
    "city" : ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)


# for saving the DataFrame to a CSV file
df.to_csv("output.csv", index=False)

df.to_excel("output.xlsx",index=False)
df.to_json("output.json", orient="records", lines=True, indent=4)