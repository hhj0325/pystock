"""
选取发布时间为2018年的文章，并对其统计
"""
from pyecharts import Bar
import pandas as pd

df = pd.read_csv('sg_articles.csv', header=None, names=["title", "article", "name", "date"])

list1 = []
for j in df['date']:
    # 获取文章发布年份
    time = j.split('-')[0]
    list1.append(time)
df['year'] = list1

# 选取发布时间为2018年的文章，并对其统计
df = df.loc[df['year'] == '2018']
place_message = df.groupby(['name'])
place_com = place_message['name'].agg(['count'])
place_com.reset_index(inplace=True)
place_com_last = place_com.sort_index()
dom = place_com_last.sort_values('count', ascending=False)[0:10]

attr = dom['name']
v1 = dom['count']
bar = Bar("微信文章发布数量TOP10", title_pos='center', title_top='18', width=800, height=400)
bar.add("", attr, v1, is_convert=True, xaxis_min=10, yaxis_rotate=30, yaxis_label_textsize=10,
        is_yaxis_boundarygap=True, yaxis_interval=0, is_label_show=True, is_legend_show=False,
        label_pos='right', is_yaxis_inverse=True, is_splitline_show=False)
bar.render("微信文章发布数量TOP10.html")


