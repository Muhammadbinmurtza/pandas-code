#head() tail()   this is used to display the first and last n rows of a DataFrame.
#head(n) 5
#tail(n) 5

import pandas as pd

df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("Display 10 first rows")
print(df.head(10))


print("\nDisplay 10 last rows")
print(df.tail(10))
