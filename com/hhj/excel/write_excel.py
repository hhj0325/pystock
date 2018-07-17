import xlwt
import datetime


# 设置表格样式
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def set_date_style(name, height, num_format_str, bold=False):
    style = set_style(name, height, bold)
    style.num_format_str = num_format_str
    return style


# 写Excel
def write_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
    row0 = ["姓名", "年龄", "出生日期", "爱好"]
    colum0 = ["张三", "李四", "恋习Python", "小明", "小红", "无名"]
    # 写第一行
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    # 写第一列
    for i in range(0, len(colum0)):
        sheet1.write(i + 1, 0, colum0[i], set_style('Times New Roman', 220, True))

    sheet1.write(1, 2, datetime.datetime(2018, 10, 10), set_date_style('Times New Roman', 220, 'yyyy-mm-dd'))
    sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
    sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
    sheet1.write_merge(4, 5, 3, 3, '打篮球')

    f.add_sheet('年级', cell_overwrite_ok=True)

    f.save('D:\\test.xls')
    print('excel done')


if __name__ == '__main__':
    write_excel()
