#**********月日温度范围*************
'''
import pandas as pd
# 读取数据
df = pd.read_csv('Shanghai_updated.csv')
# 按年、月、日分组，计算每日的最大和最小T2M
df_daily = df.groupby(['YEAR', 'MO', 'DY'])['T2M'].agg(['max', 'min'])
# 计算每日的极差
df_daily['range'] = df_daily['max'] - df_daily['min']
# 按年和月分组，计算每月的平均极差
df_monthly = df_daily.groupby([ 'MO'])['range'].mean()
# # 打印每年每月每日的极差
# print(df_daily['range'] )
# 打印12个月每个月的极差的平均值
print(round(df_monthly,1))
'''
#**********与每月5%干球温度相对应的每日平均干（湿）球温度范围*************
'''
import pandas as pd
# 读取CSV文件
data = pd.read_csv('Shanghai_updated.csv')
def calculate_percentile_temperature(month, percentile):
    # Step 1: 将实时干球温度数据T2M按月份MO分组
    monthly_t2m = data[data['MO'] == month]['T2M']
    # Step 2: 对分组后的干球温度数据T2M进行降序排列
    sorted_t2m = monthly_t2m.sort_values(ascending=False)
    # Step 3: 计算累积发生频率对应的位置索引值
    total_hours = len(sorted_t2m)
    position_index = int(total_hours * percentile)
    # Step 4: 取出相应的干球温度值作为累积发生频率对应的干球温度
    percentile_temperature = sorted_t2m.iloc[position_index]
    # Step 5: 找到该月中每天的最高温度大于累积发生频率的干球温度的所有天数
    selected_days = data[(data['MO'] == month) & (data['T2M'] > percentile_temperature)]['DY'].nunique()
    # Step 6: 求这些天每日的最大干球温度与最小干球温度之差再取平均
    max_t2m = data[(data['MO'] == month) & (data['T2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['T2M'].max()
    min_t2m = data[(data['MO'] == month) & (data['T2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['T2M'].min()
    t2m_difference =( (max_t2m - min_t2m).sum())/selected_days
    # Step 7: 求这些天每日的最大湿球温度与最小湿球温度之差再取平均
    max_wb2m = data[(data['MO'] == month) & (data['T2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['WB2M'].max()
    min_wb2m = data[(data['MO'] == month) & (data['T2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['WB2M'].min()
    wb2m_difference =( (max_wb2m - min_wb2m).sum())/selected_days
    return percentile_temperature, selected_days, t2m_difference, wb2m_difference
# 计算1-12月的值
for month in range(1, 13):
    print(f"------ 月份 {month} ------")
    percentile_temperature, selected_days, t2m_difference, wb2m_difference = calculate_percentile_temperature(month=month, percentile=0.05)
    print(f"在选定月份内，有 {selected_days} 天的最高温度大于 5% 累积发生频率的干球温度")
    print(f"5% 累积发生频率对应的干球温度: {percentile_temperature:.1f} °C")
    print(f"月最大干球温度与最小干球温度之差的平均值: {t2m_difference:.1f} °C")
    print(f"月最大湿球温度与最小湿球温度之差的平均值: {wb2m_difference:.1f} °C")

'''
#**********与每月5%湿球温度相对应的每日平均干（湿）球温度范围*************
'''
import pandas as pd
# 读取CSV文件
data = pd.read_csv('Shanghai_updated.csv')
def calculate_percentile_temperature(month, percentile):
    # Step 1: 将实时干球温度数据T2M按月份MO分组
    monthly_t2m = data[data['MO'] == month]['WB2M']
    # Step 2: 对分组后的干球温度数据T2M进行降序排列
    sorted_t2m = monthly_t2m.sort_values(ascending=False)
    # Step 3: 计算累积发生频率对应的位置索引值
    total_hours = len(sorted_t2m)
    position_index = int(total_hours * percentile)
    # Step 4: 取出相应的湿球温度值作为累积发生频率对应的湿球温度
    percentile_temperature = sorted_t2m.iloc[position_index]
    # Step 5: 找到该月中每天的最高温度大于累积发生频率的湿球温度的所有天数
    selected_days = data[(data['MO'] == month) & (data['WB2M'] > percentile_temperature)]['DY'].nunique()
    # Step 6: 求这些天每日的最大干球温度与最小干球温度之差再取平均
    max_t2m = data[(data['MO'] == month) & (data['WB2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['T2M'].max()
    min_t2m = data[(data['MO'] == month) & (data['WB2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['T2M'].min()
    t2m_difference =( (max_t2m - min_t2m).sum())/selected_days
    # Step 7: 求这些天每日的最大湿球温度与最小湿球温度之差再取平均
    max_wb2m = data[(data['MO'] == month) & (data['WB2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['WB2M'].max()
    min_wb2m = data[(data['MO'] == month) & (data['WB2M'] > percentile_temperature)].groupby(['YEAR', 'MO', 'DY'])['WB2M'].min()
    wb2m_difference = ((max_wb2m - min_wb2m).sum())/selected_days
    return percentile_temperature, selected_days, t2m_difference, wb2m_difference
# 计算1-12月的值
for month in range(1, 13):
    print(f"------ 月份 {month} ------")
    percentile_temperature, selected_days, t2m_difference, wb2m_difference = calculate_percentile_temperature(month=month, percentile=0.05)
    print(f"在选定月份内，有 {selected_days} 天的最高温度大于 5% 累积发生频率的湿球温度")
    print(f"5% 累积发生频率对应的湿球温度: {percentile_temperature:.1f} °C")
    print(f"月最大干球温度与最小干球温度之差的平均值: {t2m_difference:.1f} °C")
    print(f"月最大湿球温度与最小湿球温度之差的平均值: {wb2m_difference:.1f} °C")
'''
