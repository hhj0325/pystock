"""
代码缺失，无法run

from pyecharts import Geo, Bar
from pyecharts.echarts import style

geo = Geo('《毒液》观众位置分布', '数据来源：猫眼-Ryan采集', **style.init_style)
attr, value = geo.cast(data)
geo.add('', attr, value, visual_range=[0, 1000],
        visual_text_color='#fff', symbol_size=15,
        is_visualmap=True, is_piecewise=False, visual_split_number=10)
geo.render('观众位置分布-地理坐标图.html')

data_top20 = Counter(cities).most_common(20)
bar = Bar('《毒液》观众来源排行TOP20', '数据来源：猫眼-Ryan采集', title_pos='center', width=1200, height=600)
attr, value = bar.cast(data_top20)
bar.add('', attr, value, is_visualmap=True, visual_range=[0, 3500], visual_text_color='#fff', is_more_utils=True,
        is_label_show=True)
bar.render('观众来源排行-柱状图.html')
"""
