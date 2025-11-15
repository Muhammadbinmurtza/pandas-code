# sorting data
# A, B , C D  ..  filter in an order called sorting data 

# Sorting data in 1 column sort_values()

# df.sort_values(by = "column Name", ascending =True/False, inpace = True / False)

import pandas as pd

data = {
    "Name" : ["muhammad","ahmad", "umar"],
    "age" : [28,34,22],
    "salary" : [10000,20000,30000]
    }

df = pd.DataFrame(data)
print("data before sorting")
print(df)

df.sort_values(by=['age','salary'],ascending=[True,True],inplace=True) # in ascending pass for the number of columns you wanna sort
print("data after sorting age and salary column by descending")
print(df)

