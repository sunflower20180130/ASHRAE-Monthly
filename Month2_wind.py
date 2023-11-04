import pandas as pd
import numpy as np
import calendar  # 用于获取每个月的实际天数
import math
input_files="Shanghai_updated.csv"
def calculate_monthly_avg_wind_speed(input_file):
    # 读取数据文件
    data = pd.read_csv(input_file)
    # 提取年、月、日、时信息
    data['YEAR'] = data['YEAR'].astype(int)
    data['MO'] = data['MO'].astype(int)
    data['DY'] = data['DY'].astype(int)
    data['HR'] = data['HR'].astype(int)
    # 分组计算每个月的风速平均值
    monthly_avg_ws = data.groupby(['YEAR', 'MO'])['WS10M'].mean()
    # 计算累年每月的风速平均值
    yearly_monthly_avg_ws = monthly_avg_ws.groupby('MO').mean()
    # 计算累年平均风速
    yearly_avg_ws = data['WS10M'].mean()
    # 将结果存储到字典中
    result_dict = {
        'Yearly_Monthly_Avg_Wind_Speed': yearly_monthly_avg_ws.to_dict(),
        'Yearly_Avg_Wind_Speed': yearly_avg_ws
    }
    return result_dict

result = calculate_monthly_avg_wind_speed(input_files)  # Wind
print("Yearly Monthly Average Wind Speed:")  # Wind
for month, avg_ws in result ['Yearly_Monthly_Avg_Wind_Speed'].items():  # Wind
    print(f"Month {month}: {avg_ws:.1f}")  # Wind
print("Yearly Average Wind Speed: {:.1f}".format(result ['Yearly_Avg_Wind_Speed']))  # Wind
