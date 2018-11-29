"""
选取发布时间为2018年的文章，并对其进行月份统计
"""
import numpy as np
import pandas as pd
from pyecharts import Bar

df = pd.read_csv('sg_articles.csv', header=None, names=["title", "article", "name", "date"])

list1 = []
list2 = []
for j in df['date']:
    # 获取文章发布年份及月份
    time_1 = j.split('-')[0]
    time_2 = j.split('-')[1]
    list1.append(time_1)
    list2.append(time_2)
df['year'] = list1
df['month'] = list2

# 选取发布时间为2018年的文章，并对其进行月份统计
df = df.loc[df['year'] == '2018']
month_message = df.groupby(['month'])
month_com = month_message['month'].agg(['count'])
month_com.reset_index(inplace=True)
month_com_last = month_com.sort_index()

attr = ["{}".format(str(i) + '月') for i in range(1, 12)]
v1 = np.array(month_com_last['count'])
v1 = ["{}".format(int(i)) for i in v1]
bar = Bar("微信文章发布时间分布", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_stack=True, is_label_show=True)
bar.render("微信文章发布时间分布.html")