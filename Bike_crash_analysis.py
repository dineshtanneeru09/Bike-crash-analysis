import pandas as pd
dataframe = pd.read_csv("bike_crash.csv")

# displaying the first few rows
print(dataframe.head())

# displaying the end few rows
print(dataframe.tail())

# displaying the two cols
df_select = dataframe[['Weather Condition', 'Person Helmet']]
print(df_select)