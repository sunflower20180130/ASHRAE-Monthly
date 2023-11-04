#*******************绘制年平均温度曲线
'''
import matplotlib.pyplot as plt
# 年份和平均干球温度数据
years = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
years_short = [str(year)[-2:] for year in years]  # 提取年份后两位
avg_temperatures = [17.0, 16.9, 17.3, 16.7, 17.3, 17.4, 16.5, 16.8, 16.3, 16.4, 16.3, 17.0, 16.6, 16.6, 17.2, 17.2, 17.4, 17.1, 17.3, 17.8]
# 绘制线性图
plt.figure(figsize=(4, 3))
plt.plot(years_short, avg_temperatures, marker='o',markersize=4 , linewidth=1, color='black', label='Yearly Average Temperature')
plt.xlabel('Year', fontsize=10)
plt.ylabel('Temperature /°C', fontsize=10)
plt.tick_params(axis='x', labelsize=8)  # 设置x轴标签字体大小
plt.tick_params(axis='y', labelsize=8)  # 设置y轴标签字体大小
# plt.title('Yearly Average Temperature (2002-2021)', fontsize=10)
# 设置横坐标最后一个刻度为 21
plt.xlim(years_short [0], years_short [-1])
# 设置坐标刻度向内
plt.tick_params(axis='both', direction='in')
# 显示图例
plt.legend()
# 显示图形
plt.tight_layout()
plt.show()
'''
#*******************绘制年平均温度和标准差曲线
'''
import matplotlib.pyplot as plt
# 年份和平均干球温度、温度标准差数据
years = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
years_short = [str(year)[-2:] for year in years]  # 提取年份后两位
avg_temperatures = [17.0, 16.9, 17.3, 16.7, 17.3, 17.4, 16.5, 16.8, 16.3, 16.4, 16.3, 17.0, 16.6, 16.6, 17.2, 17.2, 17.4, 17.1, 17.3, 17.8]
std_temperatures = [8.5, 9.7, 9.3, 10.2, 9.2, 9.0, 9.7, 9.5, 9.5, 9.9, 9.6, 10.1, 8.7, 8.6, 9.3, 9.3, 9.5, 8.6, 8.5, 9.0]
# 绘制线性图
plt.figure(figsize=(8, 6))
# 绘制平均温度曲线
plt.plot(years_short, avg_temperatures, marker='o', markersize=4, linewidth=1, color='black', label='Yearly Average Temperature')
# 绘制温度标准差曲线
plt.plot(years_short, std_temperatures, marker='^', markersize=4, linewidth=1, color='black', label='Yearly Temperature Std')
plt.xlabel('Year', fontsize=10)
plt.ylabel('Temperature (°C)', fontsize=10)
plt.tick_params(axis='x', labelsize=8)  # 设置x轴标签字体大小
plt.tick_params(axis='y', labelsize=8)  # 设置y轴标签字体大小
plt.title('Yearly Average Temperature and Temperature Std (2002-2021)', fontsize=12, fontproperties='SimSun')
# 设置横坐标最后一个刻度为 21
plt.xlim(years_short[0], years_short[-1])
# 设置坐标刻度向内
plt.tick_params(axis='both', direction='in')
# 显示图例
plt.legend( fontsize=10)
# 显示图形
plt.tight_layout()
plt.show()
'''
#*******************绘制历年1月和7月平均温度
'''
import matplotlib.pyplot as plt
# 年份数据
years = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
years_short = [str(year)[-2:] for year in years]  # 提取年份后两位
# 1月和7月的温度数据
january_temperatures = [5.9, 3.2, 3.8, 3.0, 5.5, 4.6, 3.7, 3.1, 4.4, 0.8, 3.9, 3.6, 5.8, 5.4, 4.0, 6.2, 3.9, 5.6, 6.8, 4.8]
july_temperatures = [27.3, 29.3, 29.2, 29.4, 28.4, 29.2, 28.8, 28.2, 27.9, 28.8, 28.8, 30.5, 27.3, 26.1, 29.1, 30.0, 29.1, 27.2, 26.6, 28.3]
# 绘制曲线图
plt.figure(figsize=(4,3))
plt.plot(years, january_temperatures, marker='o',  markersize=3, linewidth=0.5, label='Jan AvgTem', color='black')
plt.plot(years, july_temperatures, marker='^',  markersize=3, linewidth=0.5,  label='Jul AvgTem', color='black')
# 设置图表标题和标签
plt.title('年份与温度变化', fontproperties='SimSun', fontsize=8)
plt.xlabel('Year', fontproperties='Times New Roman', fontsize=8)
plt.ylabel('Temp /°C', fontproperties='Times New Roman', fontsize=8)
plt.tick_params(axis='x', labelsize=6)  # 设置x轴标签字体大小
plt.tick_params(axis='y', labelsize=6)  # 设置y轴标签字体大小
plt.xticks(years, years_short)
# 添加这一行
plt.xlim(years[0], years[-1])
# 设置坐标刻度向内
plt.tick_params(axis='both', direction='in')
# 添加图例
plt.legend(prop={'family': 'SimSun', 'size': 8})
# 显示图形
plt.show()
'''
#*******************绘制历年1月和7月平均温度标准差
'''
import matplotlib.pyplot as plt
# 年份数据
years = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
# 1月和7月的温度标准差数据
january_std = [5, 3.91, 4.2, 3.05, 4.16, 3.25, 4.11, 4.16, 4.31, 2.62, 3.24, 3.95, 4.18, 3.72, 4.72, 4.04, 3.98, 3.04, 3.62, 5.16]
july_std = [3.29, 3.14, 3.56, 3.25, 2.23, 2.69, 2.36, 3.2, 2.33, 2.59, 2.41, 3.24, 2.7, 3.54, 2.88, 3.08, 2.72, 3.45, 2.57, 2.04]
# 绘制曲线
plt.figure(figsize=(10, 6))
plt.plot(years, january_std, marker='o', label='1月标准差', color='blue')
plt.plot(years, july_std, marker='o', label='7月标准差', color='red')
# 添加标题和标签
plt.title('1月和7月温度标准差变化', fontsize=16)
plt.xlabel('年份', fontsize=12)
plt.ylabel('温度标准差', fontsize=12)
# 添加图例
plt.legend()
# 显示图形
plt.grid(True)
plt.tight_layout()
plt.show()
'''
#*******************绘制不同统计期的HDD
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
HDD10_94_19 = [157, 103, 33, 2, 0, 0, 0, 0, 0, 0, 9, 92]
HDD10_02_21 = [177, 113, 42, 1, 0, 0, 0, 0, 0, 0, 10, 110]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, HDD10_94_19, marker='o', color='black', linewidth=1, label='94-19', linestyle='-', markersize=4)
plt.plot(months, HDD10_02_21, marker='^', color='black', linewidth=1, label='02-21', linestyle='-', markersize=4)
plt.xlabel('Month', fontsize=10, fontproperties='Times New Roman')
plt.ylabel('HDD10.0', fontsize=10, fontproperties='Times New Roman')
# plt.title('不同统计期的HDD曲线', fontsize=14)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
plt.grid(True)
# 设置横坐标刻度范围
plt.xlim(1, 12)
# 调整刻度线朝内
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
# 去掉背景网格
plt.grid(False)
# 显示图形
plt.show()
'''
#*******************绘制不同统计期的CDD
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
CDD18_3_94_19 = [0, 0, 2, 21, 107, 202, 351, 341, 206, 67, 7, 0]
CDD18_3_02_21 = [0, 0, 0, 9, 80, 186, 315, 318, 191, 52, 4, 0]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, CDD18_3_94_19, marker='o',color='black', linewidth=1, label='94-19', linestyle='-', markersize=4)
plt.plot(months, CDD18_3_02_21, marker='^',color='black', linewidth=1, label='02-21', linestyle='-', markersize=4)
plt.xlabel('Month', fontsize=10, fontproperties='Times New Roman')
plt.ylabel('CDD18.3', fontsize=10, fontproperties='Times New Roman')
# plt.title('不同统计期的CDD18.3曲线', fontsize=14)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
# 去掉背景网格
plt.grid(False)
# 设置横坐标刻度范围
plt.xlim(1, 12)
# 调整刻度线朝内
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
# 显示图形
plt.show()
'''
#*******************绘制不同统计期的CDH
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
CDH26_7_94_19 = [0, 0, 2, 30, 168, 514, 2294, 1968, 498, 33, 1, 0]
CDH26_7_02_21 = [0, 0, 0, 0, 3, 163, 1501, 1526, 175, 0, 0, 0]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, CDH26_7_94_19,marker='o',color='black', linewidth=1, label='94-19', linestyle='-', markersize=4)
plt.plot(months, CDH26_7_02_21, marker='^',color='black', linewidth=1, label='02-21', linestyle='-', markersize=4 )
plt.xlabel('Month', fontsize=10, fontproperties='Times New Roman', labelpad=2)
plt.ylabel('CDH26.7', fontsize=10, fontproperties='Times New Roman', labelpad=2)
# plt.title('不同统计期的CDH26.7曲线', fontsize=14)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
# 去掉背景网格
plt.grid(False)
# 设置横坐标刻度范围
plt.xlim(1, 12)
plt.ylim(0, 2400)
# 调整刻度线朝内
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
# 显示图形
plt.show()
'''
#*******************绘制不同统计期的平均风速
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
WSAvg_94_19 = [ 3.6, 3.7, 4.0, 3.9, 3.9, 3.5, 3.9, 4.1, 3.7, 3.4, 3.4, 3.4]
WSAvg_02_21 = [4.7, 4.8, 5.0, 5.0, 5.0, 4.5, 4.8, 4.9, 4.8, 4.7, 4.6, 4.8]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, WSAvg_94_19,marker='o',color='black', linewidth=1, label='94-19', linestyle='-', markersize=4)
plt.plot(months, WSAvg_02_21,marker='^',color='black', linewidth=1, label='02-21', linestyle='-', markersize=4)
plt.xlabel('Month', fontsize=10)
plt.ylabel('WSAvg/ m•s⁻¹', fontsize=10)  # 使用指数形式
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
# 去掉背景网格
plt.grid(False)
# 设置横坐标刻度范围
plt.xlim(1, 12)
# 调整刻度线朝内
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
# 显示图形
plt.show()

'''
#*******************绘制不同统计期的降水量
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
PrecAvg_94_19 = [70, 71, 94, 87, 99, 218, 146, 208, 115, 70, 63, 50]
PrecAvg_02_21 = [62, 77, 92, 94, 110, 186, 164, 171, 142, 79, 72, 48]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, PrecAvg_94_19 ,marker='o',color='black', linewidth=1, label='94-19', linestyle='-', markersize=4)
plt.plot(months, PrecAvg_02_21,marker='^',color='black', linewidth=1, label='02-21', linestyle='-', markersize=4)
plt.xlabel('Month', fontsize=10)
plt.ylabel('PrecAvg/ mm', fontsize=10)  # 使用指数形式
# plt.title('不同统计期的PrecAvg曲线', fontsize=14)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
# 去掉背景网格
plt.grid(False)
# 设置横坐标刻度范围
plt.xlim(1, 12)
# 调整刻度线朝内
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
# 显示图形
plt.show()
'''
#*******************绘制不同统计期的MDBR*************
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
PrecAvg_94_19 = [6.6, 6.9, 7.7, 8.3, 8.0, 6.5, 6.9, 6.3, 6.5, 7.2, 7.4, 7.2]
PrecAvg_02_21 = [7.4, 8.1, 8.9, 9.5, 8.9, 7.3, 6.4, 6.1, 6.6, 7.5, 7.7, 7.8]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, PrecAvg_94_19, marker='o', color='black', linewidth=1, label='94-19', linestyle='-', markersize=4)
plt.plot(months, PrecAvg_02_21, marker='^', color='black', linewidth=1, label='02-21', linestyle='--', markersize=4)
plt.xlabel('Month', fontsize=10,fontname='Times New Roman')
plt.ylabel('MDBR', fontsize=10,fontname='Times New Roman')
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
plt.grid(False)
plt.xlim(1, 12)
# 调整刻度线朝内
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
# 显示图形
plt.show()
'''
#*******************绘制不同统计期的5%DB MCDBR和MCWBR************
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
MCDBR_94_19 = [9.3, 10.5, 11.5, 11.5, 10.7, 9.2, 8.6, 7.7, 7.4, 8.2, 8.7, 9.1]
MCDBR_02_21 = [8.3, 9.9, 8.6, 8.1, 7.1, 5.7, 5.1, 5.0, 5.4, 6.7, 8.1, 7.2]
MCWBR_94_19 = [6, 6.3, 6.2, 5.9, 4.5, 3.6, 3, 2.8, 2.9, 3.6, 4.4, 5.7]
MCWBR_02_21 = [4.7, 5.3, 4.9, 3.7, 2.8, 2.1, 1.7, 1.8, 2.0, 2.7, 3.3, 4.2]
# 绘图
plt.figure(figsize=(5, 4))
plt.plot(months, MCDBR_94_19, marker='o', color='black', linewidth=1, label='MCDBR 94-19', linestyle='-', markersize=4)
plt.plot(months, MCDBR_02_21, marker='^', color='black', linewidth=1, label='MCDBR 02-21', linestyle='--', markersize=4)
plt.plot(months, MCWBR_94_19, marker='s', color='black', linewidth=1, label='MCWBR 94-19', linestyle='-', markersize=4)
plt.plot(months, MCWBR_02_21, marker='d', color='black', linewidth=1, label='MCWBR 02-21', linestyle='--', markersize=4)
plt.xlabel('Month', fontsize=12, fontname='Times New Roman')
plt.ylabel('Temperature/ ℃', fontsize=12, fontname='Times New Roman')
plt.xticks(months, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
plt.grid(False)
plt.xlim(1, 12)
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
plt.show()
'''
#*******************绘制不同统计期的5%WB MCDBR和MCWBR************
'''
import matplotlib.pyplot as plt
# 数据
periods = ['94-19', '02-21']
months = list(range(1, 13))
MCDBR_94_19 = [7.4, 9.3, 10, 9.7, 8.1, 7.8, 7.8, 7.2, 6.5, 6.4, 6.3, 6.7]
MCWBR_94_19 = [5.8, 6.5, 6.6, 6.1, 4.7, 3.7, 3.3, 3.1, 2.9, 3.6, 4.4, 5.7]
MCDBR_02_21 = [10.3, 11.2, 11.6, 11.1, 10.6, 11.7, 9.8, 9.7, 7.8, 11.6, 9.1, 8.3]
MCWBR_02_21 = [6, 6.1, 5.7, 4.3, 3.3, 2.7, 1.4, 1.3, 1.3, 3.8, 3.2, 4]
# 绘图
plt.figure(figsize=(5, 4))
plt.plot(months, MCDBR_94_19, marker='o', color='black', linewidth=1, label='MCDBR 94-19', linestyle='-', markersize=4)
plt.plot(months, MCWBR_94_19, marker='s', color='black', linewidth=1, label='MCWBR 94-19', linestyle='-', markersize=4)
plt.plot(months, MCDBR_02_21, marker='^', color='black', linewidth=1, label='MCDBR 02-21', linestyle='--', markersize=4)
plt.plot(months, MCWBR_02_21, marker='d', color='black', linewidth=1, label='MCWBR 02-21', linestyle='--', markersize=4)
plt.xlabel('Month', fontsize=12, fontname='Times New Roman')
plt.ylabel('Temperature/ ℃', fontsize=12, fontname='Times New Roman')
plt.xticks(months, fontsize=10)
plt.yticks(fontsize=10)
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
plt.grid(False)
plt.xlim(1, 12)
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
plt.show()
'''
#******************02-21统计期里的HDD************
'''
import matplotlib.pyplot as plt

# 数据
months = list(range(1, 13))
HDD10 = [177, 113, 42, 1, 0, 0, 0, 0, 0, 0, 10, 110]
HDD18 = [431, 340, 257, 96, 5, 0, 0, 0, 0, 19, 144, 357]

# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, HDD10, marker='o', color='black', linewidth=1, label='HDD10.0', linestyle='-', markersize=4)
plt.plot(months, HDD18, marker='^', color='black', linewidth=1, label='HDD18.3', linestyle='--', markersize=4)

plt.xlabel('Month', fontsize=10, fontname='Times New Roman')
plt.ylabel('HDD/ ℃•d', fontsize=10, fontname='Times New Roman')
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)

# 调整纵坐标刻度密度和标签
plt.yticks(ticks=range(0, 451, 50), labels=[str(i) for i in range(0, 451, 50)], fontsize=8)
# 隐藏右侧和上侧的坐标轴
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
plt.grid(False)
plt.xlim(1, 12)
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
plt.show()
'''
#******************02-21统计期里的CDH************
'''
import matplotlib.pyplot as plt
# 数据
months = list(range(1, 13))
CDH23_3 = [0, 0, 0, 1, 117, 1148, 3862, 3918, 1279, 90, 0, 0]
CDH26_7 = [0, 0, 0, 0, 3, 163, 1501, 1526, 175, 0, 0, 0]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, CDH23_3, marker='o', color='black', linewidth=1, label='CDH23.3', linestyle='-', markersize=4)
plt.plot(months, CDH26_7, marker='^', color='black', linewidth=1, label='CDH26.7', linestyle='--', markersize=4)
plt.xlabel('Month', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.ylabel('CDH / ℃•h', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
# 调整纵坐标刻度密度和标签
plt.yticks(ticks=range(0, 4501, 500), labels=[str(i) for i in range(0, 4501, 500)], fontsize=8)
# 隐藏右侧和上侧的坐标轴
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
# 设置图例位置为左上角，分成两列显示
plt.legend(prop={'family': 'Times New Roman', 'size': 8}, loc='upper left', ncol=2)
plt.grid(False)
plt.xlim(1, 12)
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
plt.show()
'''
#******************02-21统计期里的WSAvg***********
'''
import matplotlib.pyplot as plt
# 数据
months = list(range(1, 13))
WSAvg = [4.7, 4.8, 5.0, 5.0, 5.0, 4.5, 4.8, 4.9, 4.8, 4.7, 4.6, 4.8]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, WSAvg, marker='o', color='black', linewidth=1, label='WSAvg', linestyle='-', markersize=4)
plt.xlabel('Month', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.ylabel('WSAvg / m/s', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
# 调整纵坐标刻度密度和标签
plt.yticks(ticks=[i for i in range(4, 7)], labels=[str(i) for i in range(4, 7)], fontsize=8)
# 隐藏右侧和上侧的坐标轴
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.legend(prop={'family': 'Times New Roman', 'size': 8})
plt.grid(False)
plt.xlim(1, 12)
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
plt.show()
'''
#******************02-21统计期里的Pre***********
'''
import matplotlib.pyplot as plt
# 数据
months = list(range(1, 13))
PrecAvg = [62, 77, 92, 94, 110, 186, 164, 171, 142, 79, 72, 48]
PrecMax = [136, 162, 202, 184, 213, 410, 458, 297, 290, 252, 152, 141]
PrecMin = [14, 21, 36, 41, 28, 33, 57, 35, 38, 11, 13, 6]
# 绘图
plt.figure(figsize=(4, 3))
plt.plot(months, PrecAvg, marker='o', color='black', linewidth=1, label='PrecAvg', linestyle='-', markersize=4)
plt.plot(months, PrecMax, marker='^', color='black', linewidth=1, label='PrecMax', linestyle='--', markersize=4)
plt.plot(months, PrecMin, marker='s', color='black', linewidth=1, label='PrecMin', linestyle='-.', markersize=4)
plt.xlabel('Month', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.ylabel('Precipitation / mm', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
# 调整纵坐标刻度密度和标签
plt.yticks(ticks=range(0, 501, 100), labels=[str(i) for i in range(0, 501, 100)], fontsize=8)
# 隐藏右侧和上侧的坐标轴
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
# 设置图例位置为左上角，分成两列显示
plt.legend(prop={'family': 'Times New Roman', 'size': 8}, loc='upper left')
plt.grid(False)
plt.xlim(1, 12)
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
plt.show()
'''
#******************02-21统计期里的DB and MCWB***********

import matplotlib.pyplot as plt
# 数据
months = list(range(1, 13))
# DB 数据
DB = [11.4, 13.9, 18.4, 23.5, 27.7, 30.6, 34.1, 33.7, 30.5, 25.8, 21, 14.1]
# MCWB 数据
MCWB = [9.9, 12, 13.9, 17.9, 20.6, 25, 26.7, 26.8, 25.3, 19.8, 16, 12.2]
# WB 数据
WB = [9.5, 11.5, 15.1, 19.2, 22.3, 26.2, 27.7, 27.6, 25.9, 22.4, 18.1, 11.8]
# MCDB 数据
MCDB = [10.3, 12.5, 17.6, 22.7, 23.5, 29.0, 30.8, 30.8, 28.8, 24.4, 20.6, 13.4]
# 绘图
plt.figure(figsize=(6, 4))
plt.plot(months, DB, marker='o', color='black', linewidth=1, label='DB', linestyle='-', markersize=4)
plt.plot(months, MCWB, marker='o', color='black', linewidth=1, label='MCWB', linestyle='--', markersize=4)
plt.plot(months, WB, marker='^', color='black', linewidth=1, label='WB', linestyle='-', markersize=4)
plt.plot(months, MCDB, marker='^', color='black', linewidth=1, label='MCDB', linestyle='--', markersize=4)
plt.xlabel('Month', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.ylabel('Temperature / ℃', fontsize=10, fontname='Times New Roman', labelpad=1)
plt.xticks(months, fontsize=8)
plt.yticks(fontsize=8)
# 隐藏右侧和上侧的坐标轴
plt.gca().spines['right'].set_color('none')
plt.gca().spines['top'].set_color('none')
# 调整纵坐标刻度密度和标签
plt.yticks(ticks=range(5, 41, 5), labels=[str(i) for i in range(5, 41, 5)], fontsize=8)
# 设置图例位置为左上角，分成两列显示
plt.legend(prop={'family': 'Times New Roman', 'size': 8}, loc='upper left', ncol=2)
plt.grid(False)
plt.xlim(1, 12)
ax = plt.gca()
ax.tick_params(axis='both', direction='in')
plt.show()
