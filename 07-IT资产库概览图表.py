import pandas as pd
import numpy as np
import time
from datetime import date
import datetime, os, openpyxl
import xlsxwriter

# 准备EXCEL图表文件
workbook = xlsxwriter.Workbook('D:/IT资产库概览图表.xlsx')
worksheet = workbook.add_worksheet()
# chart=workbook.add_chart({'type':'column'})
# chart1=workbook.add_chart({'type':'column'})
# chart2=workbook.add_chart({'type':'column'})
# line_chart2=workbook.add_chart({'type':'line'})
# chart3=workbook.add_chart({'type':'line'})
# chart4=workbook.add_chart({'type':'pie'})

# 设置单元格格式
format = workbook.add_format()
format.set_border(1)

title_format = workbook.add_format()
title_format.set_border(1)
title_format.set_bg_color('#cccccc')
title_format.set_align('center')
title_format.set_bold()

ave_format = workbook.add_format()
ave_format.set_border(1)
# ave_format.set_num_format('0.00')


zck = pd.read_excel(r'c://downloads/资产库 (14).xls', dtype={'购买时间': date})
zck['Year'] = pd.DatetimeIndex(zck.购买时间).year
zck['Count'] = 1  # 写入一个值为1的数据列便于用pandas的pivot_table进行统计
zck.set_index('系统编号', inplace=True)
zck.姓名.fillna(r'备用机', inplace=True)

total = zck[['类别细分', 'Year', 'Count']].groupby(['类别细分', 'Year']).count()
catgory_list = ['笔记本电脑', '台式机', '打印机', '显示器', '服务器', '其他', '网络设备']
catgory_amount = len(catgory_list)
# current_year = datetime.datetime.now().year   #获取当前年份
tmp = total.query('(类别细分=="笔记本电脑")' + 'and' + '(Year == 2017)')
# tmp.Count.sum()

x = 2

# 获取每个分别名称
for cg in catgory_list:
    current_year = datetime.datetime.now().year
    row_list = []
    title_list = ['资产类别']
    tmp_total = total.query('类别细分==@cg')
    ttt = tmp_total.Count.sum()

    # 获取每个年份的合计数
    for i in range(0, 12):
        if i < 11:
            title_list.append(str(current_year))
            tmp = total.query('(类别细分==@cg)' + 'and' + '(Year == @current_year)')
            tt = tmp.Count.sum()
            row_list.append(tt)
            current_year = current_year - 1
        else:
            title_list.append('Earlier')
            tmp = total.query('(类别细分==@cg)' + 'and' + '(Year <= @current_year)')
            tt = tmp.Count.sum()
            row_list.append(tt)
            current_year = current_year - 1

    row_list.append(ttt)  # 追加合计列
    title_list.append('合  计')

    # 写入统计数据
    worksheet.write_row('B%d' % x, row_list, format)
    #     print('B%d'%x)
    print(row_list)
    x = x + 1

# 写数据
# print(title_list)

worksheet.write_row('A1', title_list, title_format)
worksheet.write_column('A2', catgory_list, format)

# 自定义样式，加粗
bold = workbook.add_format({'bold': 1})

# ***************************************
# 创建一个柱状图(column chart)
chart1 = workbook.add_chart({'type': 'column'})

# 配置第一个系列数据
chart1.add_series({
    # 这里的sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
    # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
    'name': '=Sheet1!$A$2',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$2:$M$2',
    'data_labels': {'value': 'True'},
    'line': {'color': 'red'},
})

# 配置第二个系列数据(用了另一种语法)
chart1.add_series({
    'name': '=Sheet1!$A$3',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$3:$M$3',
    'data_labels': {'value': 'True'},
    'line': {'color': 'yellow'},
})
chart1.add_series({
    'name': '=Sheet1!$A$4',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$4:$M$4',
    'data_labels': {'value': 'True'},
    'line': {'color': 'yellow'},
})
chart1.add_series({
    'name': '=Sheet1!$A$5',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$5:$M$5',
    'data_labels': {'value': 'True'},
    'line': {'color': 'yellow'},
})

# # 配置第三个系列数据(用了另一种语法)
# chart1.add_series({
#     'name': '=Sheet1!$A$4',
#     'categories': '=Sheet1!$B$1:$M$1',
#     'values':   '=Sheet1!$B$4:$M$4',
#     'data_labels':{'value':'True'},
#     'line': {'color': 'yellow'},
# })

# 设置图表的title 和 x，y轴信息
chart1.set_title({'name': '主要电脑设备概况'})
chart1.set_x_axis({'name': '年份'})
chart1.set_y_axis({'name': '数量：台'})
chart1.set_size({'width': 850, 'height': 300})

# 设置图表的风格
chart1.set_style(4)

# 把图表插入到worksheet以及偏移
worksheet.insert_chart('A10', chart1, {'x_offset': 25, 'y_offset': 10})

# ****************************
# 创建一个饼图(pie chart)
chart2 = workbook.add_chart({'type': 'pie'})

# 配置第一个系列数据
chart2.add_series({
    'name': '=Sheet1!$A$2',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$2:$M$2',
    'data_labels': {'value': 'True'},

    #     'points': [
    #         {'fill': {'color': '#00CD00'}},
    #         {'fill': {'color': 'red'}},
    #         {'fill': {'color': 'yellow'}},
    #         {'fill': {'color': 'gray'}},
    #     ],

})

# 设置图表的title 和 x，y轴信息
chart2.set_title({'name': '笔记本电脑'})
chart2.set_y_axis({'name': '数量：台'})
chart2.set_size({'width': 400, 'height': 420})
# 把图表插入到worksheet以及偏移
worksheet.insert_chart('A27', chart2, {'x_offset': 25, 'y_offset': 10})

# 创建一个饼图(pie chart)
chart2_2 = workbook.add_chart({'type': 'pie'})

# 配置第一个系列数据
chart2_2.add_series({
    'name': '=Sheet1!$A$3',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$3:$M$3',
    'data_labels': {'value': 'True'},

    #     'points': [
    #         {'fill': {'color': '#00CD00'}},
    #         {'fill': {'color': 'red'}},
    #         {'fill': {'color': 'yellow'}},
    #         {'fill': {'color': 'gray'}},
    #     ],

})

# 设置图表的title 和 x，y轴信息
chart2_2.set_title({'name': '台式电脑'})
chart2_2.set_y_axis({'name': '数量：台'})
chart2_2.set_size({'width': 400, 'height': 420})

# 设置图表的风格
# chart2.set_style(20)

# 把图表插入到worksheet以及偏移
worksheet.insert_chart('H27', chart2_2, {'x_offset': 25, 'y_offset': 10})
# ****************************


# ****************************

# 创建一个折线图(line chart)
chart3 = workbook.add_chart({'type': 'line'})

chart3.add_series({
    'name': '=Sheet1!$A$2',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$2:$M$2',
    'data_labels': {'value': 'True'},
    'line': {'color': 'blue'},
})
chart3.add_series({
    'name': '=Sheet1!$A$3',
    'categories': '=Sheet1!$B$1:$M$1',
    'values': '=Sheet1!$B$3:$M$3',
    'data_labels': {'value': 'True'},
    'line': {'color': 'green'},
})

# 设置图表的title 和 x，y轴信息
chart3.set_title({'name': '电脑年份统计'})
chart3.set_x_axis({'name': '年份'})
chart3.set_y_axis({'name': '数量：台'})
chart3.set_size({'width': 850, 'height': 300})

# 设置图表的风格
# chart_col.set_style(1)

# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('A49', chart3, {'x_offset': 25, 'y_offset': 10})
workbook.close()

df = zck[((zck.类别细分 == '笔记本电脑') | (zck.类别细分 == '台式机'))]  # 准备全部电脑的数据

# xlsfile = 'e:\\itzck\IT资产库概览图表.xlsx'   #目标写入文件
rq5y = time.strftime('%Y-%m-%d', time.localtime(time.time() - 157680000))  # 得到5年前的日期：当前日期-5年（365*5*24*60*60）

# 5年以上的电脑清单，并按类别、购买时间排序：
df_5y = df[df.购买时间 < rq5y]
tmp1 = df_5y.pivot_table(index=['成本中心', '姓名', '类别细分', '品牌', '设备型号', '序列号', '购买时间'], values=["Count"], aggfunc=np.sum,
                         margins=True)
tmp1.sort_values(by='成本中心', inplace=True)

# 全部电脑使用情况
tmp2 = df.pivot_table(index=['成本中心', '姓名', '类别细分', '品牌', '设备型号', '序列号', '购买时间'], values=["Count"], aggfunc=np.sum,
                      margins=True)
# tmp1.sort_values(by='成本中心', inplace=True)

# 全部电脑使用情况
tmp3 = df.pivot_table(index=['姓名', '类别细分', '品牌', '设备型号', '序列号', '购买时间'], values=["Count"], aggfunc='count',
                      margins=True)

# 筛选资产编号不为空的数据，以便和财务系统固定资产编号对接核对；
tmp4 = zck.pivot_table(index=["资产编号", "系统编号", "类别细分", "品牌", "设备型号"], values=["Count"], aggfunc=np.sum, margins=True)

# 按品牌统计并输出数据表；
tmp5 = zck.pivot_table(index=["品牌", "类别细分", "设备型号"], values=["Count"], aggfunc=np.sum, margins=True)

# 按品牌统计并输出数据表；
tmp6 = zck[['类别细分', 'Year', 'Count']].groupby(['类别细分', 'Year']).count()

writer = pd.ExcelWriter('D:/IT资产库概览图表.xlsx', engine='openpyxl')
if os.path.exists('D:/IT资产库概览图表.xlsx') != True:
    zck.to_excel(writer, sheet_name='资产库明细数据')
    tmp1.to_excel(writer, sheet_name='5年以上电脑使用概况')
    tmp2.to_excel(writer, sheet_name='全部电脑使用概况')
    tmp3.to_excel(writer, sheet_name='员工-电脑')
    tmp4.to_excel(writer, sheet_name='财务固资对帐')
    tmp5.to_excel(writer, sheet_name='品牌统计')
    tmp6.to_excel(writer, sheet_name='资产类别年份统计')
else:
    book = openpyxl.load_workbook(writer.path)
    writer.book = book
zck.to_excel(writer, sheet_name='资产库明细数据')
tmp1.to_excel(writer, sheet_name='5年以上电脑使用概况')
tmp2.to_excel(writer, sheet_name='全部电脑使用概况')
tmp3.to_excel(writer, sheet_name='员工-电脑')
tmp4.to_excel(writer, sheet_name='财务固资对帐')
tmp5.to_excel(writer, sheet_name='品牌统计')
tmp6.to_excel(writer, sheet_name='资产类别年份统计')

writer.save()
writer.close()

print('操作成功完成！')
