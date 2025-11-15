#pd.merge(df1, df2, on = column name, how= type of join )

import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID' : [1,2,3],
    'Name' : ['umar','talha','muhammad']
})

df_order = pd.DataFrame({
    'CustomerID' : [1,2,4],
    'OrderAmount' : [250,450,350]
})

df_merged = pd.merge(df_customers,df_order, how="inner",on="CustomerID")
print("inner join")
print(df_merged)

df_merged = pd.merge(df_customers,df_order, how="outer",on="CustomerID")
print("outer join")
print(df_merged)

df_merged = pd.merge(df_customers,df_order, how="left",on="CustomerID")
print("left join")
print(df_merged)

df_merged = pd.merge(df_customers,df_order, how="right",on="CustomerID")
print("right join")
print(df_merged)