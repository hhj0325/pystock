import pandas as pd
import numpy as np

# print('----pd.Series----')
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

print('----dates----')
dates = pd.date_range(start='20130101', end='20130106')
print(dates)

print('----df----')
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# print('----df2----')
# df2 = pd.DataFrame({'A': 1.,
#                     'B': pd.Timestamp('20130102'),
#                     'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                     'D': np.array([2] * 4, dtype='int32'),
#                     'E': pd.Categorical(["test", "train", "test", "train"]),
#                     'F': 'foo1'})
# print(df2)
#
# print('----df2.dtypes----')
# print(df2.dtypes)
#
# print('----df.head()----')
# print(df.head(2))
#
# print('----df.tail()----')
# print(df.tail(2))
#
# print('----df.index----')
# print(df.index)
#
# print('----df.columns----')
# print(df.columns)

# print('----df.describe()----')
# print(df.describe())
#
# print('----df.T----')
# print(df.T)

# print('----df.(axis=1, ascending=False)----')
# print(df.sort_index(axis=0, ascending=False))

# print('----df.sort_values(\'C\')----')
# print(df.sort_values('C'))

# print('----df[\'A\']----')
# print(df['A'])
#
# print('----df[0:3]----')
# print(df[0:1])

# print('----df[\'20130102\':\'20130104\']----')
# print(df['20130102':'20130104'])

# print('----df.loc[dates[3]]----')
# print(df.loc[dates[3]])

# print('----df.loc[:, [\'A\', \'B\']]----')
# print(df.loc[:, ['A', 'B']])
#
# print('----df.loc[\'20130102\':\'20130104\', [\'A\', \'B\']]----')
# print(df.loc['20130102':'20130104', ['A', 'B']])

# print('----df.at[dates[0], \'A\']----')
# print(df.at[dates[0], 'A'])

# print('----df.iloc[3]----')
# print(df.iloc[3])
# print(df.iloc[3:5, 0:2])
# print(df.iloc[[1, 2, 4], [0, 2]])
# print(df.iloc[1:3, :])
# print(df.iloc[:, 1:3])
# print(df.iloc[1, 1])
# print(df.iat[1, 1])

# print('----df[df > 0]----')
# print(df[df > 0])

# print('----df2----')
# df2 = df.copy()
# df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
# df2[df2 > 0] = -df2
# print(df2)
# print(df2[df2['E'].isin(['two','four'])])

# df.loc[:,'D'] = np.array([5] * len(df))
# print(df)

# print(df.mean())
# print(df.mean(1))
print('----df.apply(np.cumsum)----')
print(df.apply(np.cumsum))
# s = pd.Series(np.random.randint(0, 7, size=10))
# print(s)
# print(s.value_counts())
