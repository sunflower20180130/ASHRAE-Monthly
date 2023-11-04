import pandas as pd
import numpy as np
import calendar  # 用于获取每个月的实际天数
import math
input_files="Shanghai_updated.csv"
def calculate_monthly_precipitation_stats(input_file):
    # 读取数据文件
    data = pd.read_csv(input_file)
    # 提取年、月、日、时信息
    data['YEAR'] = data['YEAR'].astype(int)
    data['MO'] = data['MO'].astype(int)
    data['DY'] = data['DY'].astype(int)
    data['HR'] = data['HR'].astype(int)
    # 分组计算每个月的降水量序列
    monthly_precipitation = data.groupby(['YEAR', 'MO'])['PRECTOTCORR'].sum()
    # 计算累年每月的平均、最大、最小降水量和降水量标准差
    yearly_monthly_avg_precip = monthly_precipitation.groupby('MO').mean().apply(int)
    yearly_monthly_max_precip = monthly_precipitation.groupby('MO').max().apply(int)
    yearly_monthly_min_precip = monthly_precipitation.groupby('MO').min().apply(int)
    yearly_monthly_std_precip = monthly_precipitation.groupby('MO').std().apply(int)
      # 将结果存储到字典中
    result_dict = {
        'Yearly_Monthly_Avg_Precipitation': yearly_monthly_avg_precip.to_dict(),
        'Yearly_Monthly_Max_Precipitation': yearly_monthly_max_precip.to_dict(),
        'Yearly_Monthly_Min_Precipitation': yearly_monthly_min_precip.to_dict(),
        'Yearly_Monthly_Std_Precipitation': yearly_monthly_std_precip.to_dict(),
    }
    return result_dict

###############3.Precipitation Auunal mm ##################
def calculate_annual_precipitation_stats(input_file):
    # 读取数据文件
    data = pd.read_csv(input_file)
    # 提取年、月、日、时信息
    data['YEAR'] = data['YEAR'].astype(int)
    data['MO'] = data['MO'].astype(int)
    data['DY'] = data['DY'].astype(int)
    data['HR'] = data['HR'].astype(int)
    # 分组计算每一年的降水量序列
    annual_precipitation = data.groupby('YEAR')['PRECTOTCORR'].sum()
    # 计算每一年的平均降水量
    yearly_avg_precipitation = annual_precipitation.mean().round(1)
    # 计算累年平均降水量、最大降水量年份、最小降水量年份
    max_precip_year = annual_precipitation.idxmax()
    max_precip_value = int(annual_precipitation[max_precip_year])
    min_precip_year = annual_precipitation.idxmin()
    min_precip_value = int(annual_precipitation[min_precip_year])
    # 计算年降水标准差
    yearly_precip_std = np.sqrt(np.sum((annual_precipitation - yearly_avg_precipitation) ** 2) / len(annual_precipitation))
    # 将结果存储到字典中
    result_dict = {
        'Yearly_Avg_Precipitation': yearly_avg_precipitation,
        'Max_Precipitation_Year': max_precip_year,
        'Max_Precipitation_Value': max_precip_value,
        'Min_Precipitation_Year': min_precip_year,
        'Min_Precipitation_Value': min_precip_value,
        'Yearly_Precipitation_Std': yearly_precip_std
    }
    return result_dict

# result = calculate_monthly_precipitation_stats(input_files) #Precipitation  Month mm
# print("Yearly Monthly Average Precipitation:")  #Precipitation  Month mm
# for month, avg_precip in result['Yearly_Monthly_Avg_Precipitation'].items():  #Precipitation  Month mm
#     print(f"Month {month}: Avg = {avg_precip}, Max = {result['Yearly_Monthly_Max_Precipitation'][month]}, "   #Precipitation  Month mm
#           f"Min = {result['Yearly_Monthly_Min_Precipitation'][month]}, Std = {result['Yearly_Monthly_Std_Precipitation'][month]}")   #Precipitation  Month mm

result = calculate_annual_precipitation_stats(input_files) #Precipitation  Annual mm
print("Yearly Average Precipitation: {:.1f} mm".format(result['Yearly_Avg_Precipitation'])) #Precipitation  Annual mm
print("Year with Max Precipitation: {} ({} mm)".format(result['Max_Precipitation_Year'], result['Max_Precipitation_Value'])) #Precipitation  Annual mm
print("Year with Min Precipitation: {} ({} mm)".format(result['Min_Precipitation_Year'], result['Min_Precipitation_Value'])) #Precipitation  Annual mm
print("Yearly Precipitation Standard Deviation: {:.2f} mm".format(result['Yearly_Precipitation_Std'])) #Precipitation  Annual mm