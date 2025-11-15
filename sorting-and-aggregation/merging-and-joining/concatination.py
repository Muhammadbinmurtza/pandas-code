"""
combining data 
vertically (row-wised)
horizontally (column-wise)

pd.concat([df1,df2], axis = 0, ignore_index = True)

"""

import pandas as pd

df_region1= pd.DataFrame({
    'CustomerID' : [1,2],
    'Name' : ['muhammad','umar']
})

df_region2 = pd.DataFrame({
    'CustomerID' : [3,4],
    'Name' : ["abdullah","zohaib"]
})

df_concat = pd.concat([df_region1,df_region2], axis=0,ignore_index=True)
print(df_concat)