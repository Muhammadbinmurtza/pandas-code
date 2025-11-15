import pandas as pd

data ={
    "time" : [1,2,3,4,5],
    "value" : [10, None, 30, None, 50],

}

df = pd.DataFrame(data)
print("before interpolation")
print(df)

df['value'] = df['value'].interpolate(method='linear')  # Interpolating missing values using linear method
print("after interpolation")    
print(df)

'''
WHEN TO USE INTERPOLATION?
1- time series data
2- numeric data with trends
3- avoid droping rows with missing values
'''