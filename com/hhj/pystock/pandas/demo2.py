import pandas as pd
import numpy as np

# df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
#                    'B': ['A', 'B', 'C'] * 4,
#                    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
#                    'D': np.random.randn(12),
#                    'E': np.random.randn(12)})
# print(df)
#
# df1 = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
# print(df1)
#
# # 生成100秒
# rng = pd.date_range('20170101', periods=100, freq='S')
# ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
# print(ts.resample('2T').sum())

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']
                   })
print(df)
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])
df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df["grade"].cat.categories)
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df["grade"])
print(df.sort_values("raw_grade"))
