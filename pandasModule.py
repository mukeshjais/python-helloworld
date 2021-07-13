import pandas as pd

data = { 
'date': ['14-07-21', '15-07-21', '14-06-21', '14-08-21', '14-09-21'], 
'state': ['IN', 'IN', 'IL', 'MN', 'FL'], 
'cases':[50, 60, 70, 60, 90],
'deaths':[50, 30, 70, 60, 90]
} 



df = pd.DataFrame(data)
df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)
df['ratio'] = df['deaths']/df['cases']

print(df[df['ratio'] == df['ratio'].max()])

#df = pd.DataFrame(data, index=['James', 'Bob', 'Amy', 'Dave'])
try:

    df['ratio'] = df['deaths']/df['cases']

except Exception as ex:
    print(str(ex))

print(df['ratio'].max())
print(df.groupby('month')['cases'].sum())

print(df['month'].value_counts())
print(df['cases'].describe())
print(df.describe())

print(type(df['ages']))


print(type(df[['ages', 'height']]))

