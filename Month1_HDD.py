import pandas as pd
import numpy as np
import calendar  # 用于获取每个月的实际天数
import math
data_file_path = "Shanghai_updated.csv"
output_mean= "Shanghai_updated_mean.csv"
#*************累年年平均温度与标准差
'''
def calculate_yearly_avg_and_std(data_file):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 计算年平均干球温度
    yearly_avg_t2m = data['T2M'].mean()
    # 计算年温度标准差
    yearly_std_t2m = data['T2M'].std()
    return yearly_avg_t2m, yearly_std_t2m

# 调用函数并传入数据文件路径
avg_t2m, std_t2m = calculate_yearly_avg_and_std(data_file_path)
print(f"年平均干球温度: {round(avg_t2m,1)}°C")
print(f"年温度标准差: {round(std_t2m,1)}°C")

'''
#*************历年年平均温度与标准差 打印在同一行
'''
def calculate_yearly_average_temperature(data_file):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 按年份分组数据
    yearly_groups = data.groupby('YEAR')
    yearly_average_temperatures = {}  # 存储每年的平均干球温度
    # 遍历每一年的数据
    for year, year_data in yearly_groups:
        # 计算每年的平均干球温度
        yearly_average_t2m = year_data['T2M'].mean()
        yearly_average_temperatures[year] = yearly_average_t2m
    return yearly_average_temperatures
def calculate_yearly_temperature_std(data_file):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 按年份分组数据
    yearly_groups = data.groupby('YEAR')
    yearly_temperature_stds = {}  # 存储每年的温度标准差
    # 遍历每一年的数据
    for year, year_data in yearly_groups:
        # 计算每年的温度标准差
        yearly_temperature_std = year_data['T2M'].std()
        yearly_temperature_stds[year] = yearly_temperature_std
    return yearly_temperature_stds

average_temperatures = calculate_yearly_average_temperature(data_file_path)
temperature_stds = calculate_yearly_temperature_std(data_file_path)
print("年份\t平均温度\t温度标准差")
for year in average_temperatures.keys():
    print(f"{year}\t{round(average_temperatures[year],1)}\t\t{round(temperature_stds[year],1)}")
'''
#*************历年年平均温度与标准差  分别打印 保留一位小数
'''
def calculate_yearly_average_temperature(data_file):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 按年份分组数据
    yearly_groups = data.groupby('YEAR')
    yearly_average_temperatures = {}  # 存储每年的平均干球温度
    # 遍历每一年的数据
    for year, year_data in yearly_groups:
        # 计算每年的平均干球温度
        yearly_average_t2m = year_data['T2M'].mean()
        yearly_average_temperatures[year] = yearly_average_t2m
    return yearly_average_temperatures
def calculate_yearly_temperature_std(data_file):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 按年份分组数据
    yearly_groups = data.groupby('YEAR')
    yearly_temperature_stds = {}  # 存储每年的温度标准差
    # 遍历每一年的数据
    for year, year_data in yearly_groups:
        # 计算每年的温度标准差
        yearly_temperature_std = year_data['T2M'].std()
        yearly_temperature_stds[year] = yearly_temperature_std
    return yearly_temperature_stds
# 文件路径
data_file_path = "Shanghai_updated.csv"
# 计算每年的平均干球温度
average_temperatures = calculate_yearly_average_temperature(data_file_path)
print("每年的平均干球温度:")
for year, temp in average_temperatures.items():
    print(f"{year}: {round(temp, 1)}")
# 计算每年的温度标准差
temperature_stds = calculate_yearly_temperature_std(data_file_path)
print("\n每年的温度标准差:")
for year, std in temperature_stds.items():
    print(f"{year}: {round(std, 1)}")
'''
#*************累年月平均温度与标准差 基于实时温度
'''
import pandas as pd
def calculate_monthly_stats(data_file):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 按月份分组数据
    monthly_groups = data.groupby('MO')
    # 存储月平均干球温度和温度标准差
    monthly_avg_t2m = {}
    monthly_std_t2m = {}
    # 遍历每个月的数据
    for month, month_data in monthly_groups:
        # 计算月平均干球温度
        monthly_avg_t2m[month] = month_data['T2M'].mean()
        # 计算温度标准差
        monthly_std_t2m[month] = month_data['T2M'].std()
    return monthly_avg_t2m, monthly_std_t2m
# 调用函数并传入数据文件路径
data_file_path = "Shanghai_updated.csv"
avg_t2m, std_t2m = calculate_monthly_stats(data_file_path)
# 打印月平均干球温度和温度标准差
print("月份\t月平均温度\t月平均温度标准差")
for month, avg_temp in avg_t2m.items():
    std_temp = std_t2m[month]
    print(f"{month}\t\t\t{round(avg_temp, 1)} \t\t \t{round(std_temp,1)} ")
'''

#*************历年1和7月平均温度与标准差
'''
import pandas as pd
data_file_path = "Shanghai_updated.csv"

def calculate_monthly_stats(data_file):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 提取年份和月份
    data['Year'] = data['YEAR']
    data['Month'] = data['MO']
    # 按年份和月份分组数据
    monthly_groups = data.groupby(['Year', 'Month'])
    # 存储结果
    results = []
    for (year, month), month_data in monthly_groups:
        # 仅保留1月和7月的数据
        if month in [1, 7]:
            # 计算每月的平均干球温度
            monthly_avg_t2m = month_data['T2M'].mean()
            # 计算每月的温度标准差
            monthly_std_t2m = month_data['T2M'].std()
            # 添加到结果中
            results.append({'Year': year, 'Month': month, 'Avg_Temperature': round(monthly_avg_t2m,1), 'Temperature_Std': round(monthly_std_t2m,2)})
    return pd.DataFrame(results)
# 调用函数并传入数据文件路径
monthly_stats = calculate_monthly_stats(data_file_path)
# 打印结果
print(monthly_stats)
'''
#************* 计算日平均温度
'''
import pandas as pd
import numpy as np
import calendar  # 用于获取每个月的实际天数
import math
def calculate_day_maxmin_std(input_file, output_file):
    # 读取原始数据文件
    data = pd.read_csv(input_file)
    # 创建一个空的DataFrame用于存储结果
    result = pd.DataFrame(columns=["Date", "DBAvg", "DBStd"])
    # 循环遍历每年、每月、每日
    for year in range(2002, 2022):
        for month in range(1, 13):
            # 获取每个月的实际天数
            days_in_month = calendar.monthrange(year, month)[1]
            # 遍历每日
            for day in range(1, days_in_month + 1):
                # 创建日期掩码以选择特定日期的数据
                date_mask = (data["YEAR"] == year) & (data["MO"] == month) & (data["DY"] == day)
                # 提取特定日期的每小时温度数据
                hourly_temperatures = data[date_mask]["T2M"]
                # 计算每天的平均温度
                daily_avg = round(hourly_temperatures.mean(), 2)
                # 计算每天的温度标准差
                diff_squared_sum = ((hourly_temperatures - daily_avg) ** 2).sum()
                daily_std = round(np.sqrt(diff_squared_sum / 24), 2)
                # 添加结果到结果DataFrame
                result = pd.concat([result, pd.DataFrame({"Date": [f"{year}/{month}/{day}"],
                                                          "DBAvg": [daily_avg],
                                                          "DBStd": [daily_std]})], ignore_index=True)
    # 将结果保存到文件
    result.to_csv(output_file, index=False)
    # 打印完成信息
    print("Calculation complete. Results have been saved to", output_file)

calculate_day_maxmin_std(data_file_path , output_mean)  # call function
'''
#************* HDD10.0 and HDD18.3
'''
import pandas as pd
import numpy as np
import calendar  # 用于获取每个月的实际天数
import math
def calculate_hdd(data, basetemp):
    # 初始化每个月的HDD值
    monthly_hdd = np.zeros(12)
    # 遍历每个月
    for month in range(1, 13):
        # 创建掩码以选择特定月份的数据
        mask = (data['MONTH'] == month)
        # 提取特定月份的每日平均温度数据
        monthly_temps = data[mask]['DBAvg'].values
        # 计算温度低于阈值的日子的差值总和
        diff_sum = np.sum(np.maximum(basetemp - monthly_temps, 0))
        # 将差值总和累加到每个月的HDD值中
        monthly_hdd[month - 1] = diff_sum
    return monthly_hdd.astype(int)
def calculate_monthly_hdd(input_file):
    # 读取数据文件
    data = pd.read_csv(input_file)
    # 提取年、月、日信息
    date_parts = data['Date'].str.split('/', expand=True)
    data['YEAR'] = date_parts[0].astype(int)
    data['MONTH'] = date_parts[1].astype(int)
    data['DAY'] = date_parts[2].astype(int)
    # 计算HDD10和HDD18.3
    hdd10 = calculate_hdd(data, 10)
    hdd18_3 = calculate_hdd(data, 18.3)
    # 计算每月的平均HDD值
    monthly_avg_hdd10 = hdd10 / 20
    monthly_avg_hdd18_3 = hdd18_3 / 20
    # 创建存储结果的字典
    monthly_hdd_dict = {}
    # 将结果存储到字典中
    for month in range(1, 13):
        monthly_hdd_dict[month] = {
            'HDD10': int(monthly_avg_hdd10[month - 1]),
            'HDD18.3': int(monthly_avg_hdd18_3[month - 1])
        }
    return monthly_hdd_dict

monthly_hdd_dict = calculate_monthly_hdd(output_mean)  #HDD10.0 and HDD18.3
for month, hdd_values in monthly_hdd_dict.items(): #HDD10.0 and HDD18.3
    print(f"Month {month}: HDD10 = {hdd_values['HDD10']}, HDD18.3 = {hdd_values['HDD18.3']}") #HDD10.0 and HDD18.3
'''
#************* CDD10.0 and CDD18.3
'''
def calculate_cdd(data, threshold):
    # 初始化每个月的CDD值
    monthly_cdd = np.zeros(12)
    # 遍历每个月
    for month in range(1, 13):
        # 创建掩码以选择特定月份的数据
        mask = (data['MONTH'] == month)
        # 提取特定月份的每日平均温度数据
        monthly_temps = data[mask]['DBAvg'].values
        # 计算温度高于阈值的日子的差值总和
        diff_sum = np.sum(np.maximum(monthly_temps - threshold, 0))
        # 将差值总和累加到每个月的CDD值中
        monthly_cdd[month - 1] = diff_sum
    return monthly_cdd.astype(int)
def calculate_monthly_cdd(input_file):
    # 读取数据文件
    data = pd.read_csv(input_file)
    # 提取年、月、日信息
    date_parts = data['Date'].str.split('/', expand=True)
    data['YEAR'] = date_parts[0].astype(int)
    data['MONTH'] = date_parts[1].astype(int)
    data['DAY'] = date_parts[2].astype(int)
    # 计算CDD10和CDD18.3
    cdd10 = calculate_cdd(data, 10)
    cdd18_3 = calculate_cdd(data, 18.3)
    # 计算每月的平均CDD值
    monthly_avg_cdd10 = cdd10 / 20
    monthly_avg_cdd18_3 = cdd18_3 / 20
    # 创建存储结果的字典
    monthly_cdd_dict = {}
    # 将结果存储到字典中
    for month in range(1, 13):
        monthly_cdd_dict[month] = {
            'CDD10': int(monthly_avg_cdd10[month - 1]),
            'CDD18.3': int(monthly_avg_cdd18_3[month - 1])
        }
    return monthly_cdd_dict

monthly_cdd_dict = calculate_monthly_cdd(output_mean) #CDD10.0 and CDD18.3
for month, cdd_values in monthly_cdd_dict.items():  #CDD10.0 and CDD18.3
    print(f"Month {month}: CDD10 = {cdd_values['CDD10']}, CDD18.3 = {cdd_values['CDD18.3']}")  #CDD10.0 and CDD18.3
'''
#************* CDH23.3 and CDH26.7

def calculate_cdh(data, threshold):
    # 初始化每个月的CDH值
    monthly_cdh = np.zeros(12)
    # 遍历每个月
    for month in range(1, 13):
        # 创建掩码以选择特定月份的数据
        mask = (data['MONTH'] == month)
        # 提取特定月份的每日平均温度数据
        monthly_temps = data[mask]['DBAvg'].values
        # 计算温度高于阈值的日子的差值总和
        diff_sum = np.sum(np.maximum(monthly_temps - threshold, 0))
        # 将差值总和累加到每个月的CDH值中
        monthly_cdh[month - 1] = diff_sum
    return monthly_cdh.astype(int)
def calculate_monthly_cdh(input_file):
    # 读取数据文件
    data = pd.read_csv(input_file)
    # 提取年、月、日信息
    date_parts = data['Date'].str.split('/', expand=True)
    data['YEAR'] = date_parts[0].astype(int)
    data['MONTH'] = date_parts[1].astype(int)
    data['DAY'] = date_parts[2].astype(int)
    # 计算CDH23.3和CDH26.7
    cdh23_3 = calculate_cdh(data, 23.3)
    cdh26_7 = calculate_cdh(data, 26.7)
    # 计算每月的平均CDH值
    monthly_avg_cdh23_3 = cdh23_3 / 20
    monthly_avg_cdh26_7 = cdh26_7 / 20
    # 创建存储结果的字典
    monthly_cdh_dict = {}
    # 将结果存储到字典中
    for month in range(1, 13):
        monthly_cdh_dict[month] = {
            'CDH23.3': int(monthly_avg_cdh23_3[month - 1]*24),
            'CDH26.7': int(monthly_avg_cdh26_7[month - 1]*24)
        }
    return monthly_cdh_dict
monthly_cdh_dict = calculate_monthly_cdh(output_mean)  #CDH23.3 and CDH26.7
for month, cdh_values in monthly_cdh_dict.items(): #CDH23.3 and CDH26.7
    print(f"Month {month}: CDH23.3 = {cdh_values['CDH23.3']}, CDH26.7 = {cdh_values['CDH26.7']}") #CDH23.3 and CDH26.7
