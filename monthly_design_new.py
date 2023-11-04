import pandas as pd
import numpy as np
import calendar  # 用于获取每个月的实际天数
import math
input_files="Shanghai_updated.csv"
output_mean= "Beijing_Day_mean.csv"
############## 0.average temperature of daily =hourly temperature.mean and std   ---采用此方法获得日平均温度##################
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

############### 0.average temperature  and std  of monthly##################
def calculate_monthly_statistics(input_file):
    # Baca file data
    data = pd.read_csv(input_file)
    # Ekstrak informasi tahun, bulan, dan hari
    date_parts = data['Date'].str.split('/', expand=True)
    data['YEAR'] = date_parts[0].astype(int)
    data['MONTH'] = date_parts[1].astype(int)
    data['DAY'] = date_parts[2].astype(int)
    # Inisialisasi hasil
    monthly_tem_avg = {}
    monthly_tem_std = {}
    # Iterasi untuk menghitung rata-rata bulanan dan standar deviasi
    for month in range(1, 13):
        mask = (data['MONTH'] == month)
        monthly_temps = data[mask]['DBAvg'].values
        monthly_avg = np.mean(monthly_temps)
        monthly_tem_avg[month] = round(monthly_avg,2)
        # Menghitung standar deviasi
        monthly_tem_diff = monthly_temps - monthly_avg
        squared_diff_sum = np.sum(monthly_tem_diff ** 2)
        monthly_tem_std[month] = round(np.sqrt(squared_diff_sum / len(monthly_temps)),1)
    # Print hasil dalam bentuk kamus
    print("Monthly Temperature Average:")
    print(monthly_tem_avg)
    print("Monthly Temperature Standard Deviation:")
    print(monthly_tem_std)

############### 0.average temperature and std  of Year ##################
def calculate_yearly_statistics(input_file):
    # 读取数据文件
    data = pd.read_csv(input_file)
    # 计算年平均温度
    yearly_avg_temp =round( data['DBAvg'].mean(),2)
    # 计算年平均温度标准差
    yearly_tem_diff = data['DBAvg'] - yearly_avg_temp
    yearly_tem_std = round(np.sqrt((yearly_tem_diff ** 2).sum() / len(data)),1)
    # 打印结果
    print("Yearly Average Temperature:", yearly_avg_temp)
    print("Yearly Temperature Standard Deviation:", yearly_tem_std)

############### 1.HDD10.0 and HDD18.3 ##################
def calculate_hdd(data, threshold):
    # 初始化每个月的HDD值
    monthly_hdd = np.zeros(12)
    # 遍历每个月
    for month in range(1, 13):
        # 创建掩码以选择特定月份的数据
        mask = (data['MONTH'] == month)
        # 提取特定月份的每日平均温度数据
        monthly_temps = data[mask]['DBAvg'].values
        # 计算温度低于阈值的日子的差值总和
        diff_sum = np.sum(np.maximum(threshold - monthly_temps, 0))
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

############### 1.CDD10.0 and CDD18.3 ##################
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

############### 1.CDH23.3 and CDH26.7 ##################
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

###############2.wind ##################
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

###############3.Precipitation Month mm ##################
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

###############4.Monthly Design Dry Bulb and Mean Coincident Wet Bulb Temperatures##################
def calculate_percentiles_DB(data, percentiles):
    sorted_data_t2m = data.sort_values(by='T2M', ascending=False)
    percentile_labels = [f"{percentile}%" for percentile in percentiles]
    percentile_values_t2m = {}
    for percentile in percentiles:
        percentile_index = int(len(sorted_data_t2m) * (percentile / 100))
        percentile_values_t2m[f"{percentile}%"] = sorted_data_t2m.iloc[percentile_index]['T2M']
    return percentile_values_t2m
def calculate_average_wb2m(data, percentile_values):
    average_wb2m_values = []
    for t2m_percentile in percentile_values.values():
        t2m_data = data[data['T2M'] == t2m_percentile]
        average_wb2m_values.append(t2m_data['WB2M'].mean())
    return average_wb2m_values
def calculate_monthly_values(data, percentiles):
    monthly_results = {}
    for month in range(1, 13):  # Loop through each month
        monthly_data = data[data['MO'] == month]
        percentile_values_t2m = calculate_percentiles_DB(monthly_data, percentiles)
        average_wb2m_values = calculate_average_wb2m(monthly_data, percentile_values_t2m)
        monthly_results[month] = {'percentiles': percentile_values_t2m, 'average_wb2m': average_wb2m_values}
    return monthly_results

###############5.Monthly Design Wet Bulb and Mean Coincident Dry Bulb Temperatures##################
def calculate_percentiles_WB(data, percentiles):
    sorted_data_wb2m = data.sort_values(by='WB2M', ascending=False)
    percentile_labels = [f"{percentile}%" for percentile in percentiles]
    percentile_values_wb2m = {}
    for percentile in percentiles:
        percentile_index = int(len(sorted_data_wb2m) * (percentile / 100))
        percentile_values_wb2m[f"{percentile}%"] = sorted_data_wb2m.iloc[percentile_index]['WB2M']
    return percentile_values_wb2m
def calculate_average_t2m(data, percentile_values):
    average_t2m_values = []
    for wb2m_percentile in percentile_values.values():
        wb2m_data = data[data['WB2M'] == wb2m_percentile]
        average_t2m_values.append(wb2m_data['T2M'].mean())
    return average_t2m_values
def calculate_monthly_values_2(data, percentiles):
    monthly_results = {}
    for month in range(1, 13):  # Loop through each month
        monthly_data = data[data['MO'] == month]
        percentile_values_wb2m = calculate_percentiles_WB(monthly_data, percentiles)
        average_t2m_values = calculate_average_t2m(monthly_data, percentile_values_wb2m)
        monthly_results[month] = {'percentiles': percentile_values_wb2m, 'average_t2m': average_t2m_values}
    return monthly_results

###############6.Mean Daily Temperature Range ##################
'''
import pandas as pd

# 读取 CSV 文件
data = pd.read_csv("Beijing_with_properties.csv")

# 将日期列转换为日期时间对象
data['Date'] = pd.to_datetime(data[['YEAR', 'MO', 'DY', 'HR']], format='%Y-%m-%d %H')

# 分组数据，按月份
monthly_groups = data.groupby(data['Date'].dt.strftime('%Y-%m'))

monthly_mbr = {}  # 存储每月的 MDBR

# 遍历每个月的数据
for month, month_data in monthly_groups:

    # 计算每日的最大和最小干球温度
    daily_max_t2m = month_data.groupby(month_data['Date'].dt.day)['T2M'].max()
    daily_min_t2m = month_data.groupby(month_data['Date'].dt.day)['T2M'].min()

    # 计算每日的干球温度范围
    daily_t2m_range = daily_max_t2m - daily_min_t2m

    # 计算每月的 MDBR
    monthly_mbr[month] = daily_t2m_range.mean()

# 打印每月的 MDBR
for month, mbr in monthly_mbr.items():
    print(f"{month}: {mbr:.2f}")
'''
###############7.Clear Sky Solar Irradiance ##################

###############8.All-Sky Solar Radiation ##################

if __name__ == '__main__':
    ## Annual Month DBAvg and DBStd 24mean
    # calculate_day_maxmin_std(input_files, output_mean)  # call function
    # calculate_monthly_statistics(output_mean)  #verage temperature  and std  of monthly
    # calculate_yearly_statistics(output_mean)  #average temperature and std  of Year

    monthly_hdd_dict = calculate_monthly_hdd(output_mean)  #HDD10.0 and HDD18.3
    for month, hdd_values in monthly_hdd_dict.items(): #HDD10.0 and HDD18.3
        print(f"Month {month}: HDD10 = {hdd_values['HDD10']}, HDD18.3 = {hdd_values['HDD18.3']}") #HDD10.0 and HDD18.3

    # monthly_cdd_dict = calculate_monthly_cdd(output_mean) #CDD10.0 and CDD18.3
    # for month, cdd_values in monthly_cdd_dict.items():  #CDD10.0 and CDD18.3
    #     print(f"Month {month}: CDD10 = {cdd_values['CDD10']}, CDD18.3 = {cdd_values['CDD18.3']}")  #CDD10.0 and CDD18.3

    # monthly_cdh_dict = calculate_monthly_cdh(output_mean)  #CDH23.3 and CDH26.7
    # for month, cdh_values in monthly_cdh_dict.items(): #CDH23.3 and CDH26.7
    #     print(f"Month {month}: CDH23.3 = {cdh_values['CDH23.3']}, CDH26.7 = {cdh_values['CDH26.7']}") #CDH23.3 and CDH26.7

    # result = calculate_monthly_avg_wind_speed(input_files)  # Wind
    # print("Yearly Monthly Average Wind Speed:")  # Wind
    # for month, avg_ws in result['Yearly_Monthly_Avg_Wind_Speed'].items():  # Wind
    #     print(f"Month {month}: {avg_ws:.1f}")  # Wind
    # print("Yearly Average Wind Speed: {:.1f}".format(result['Yearly_Avg_Wind_Speed']))  # Wind
    #
    # result = calculate_monthly_precipitation_stats(input_files) #Precipitation  Month mm
    # print("Yearly Monthly Average Precipitation:")  #Precipitation  Month mm
    # for month, avg_precip in result['Yearly_Monthly_Avg_Precipitation'].items():  #Precipitation  Month mm
    #     print(f"Month {month}: Avg = {avg_precip}, Max = {result['Yearly_Monthly_Max_Precipitation'][month]}, "   #Precipitation  Month mm
    #           f"Min = {result['Yearly_Monthly_Min_Precipitation'][month]}, Std = {result['Yearly_Monthly_Std_Precipitation'][month]}")   #Precipitation  Month mm
    #
    #     result = calculate_annual_precipitation_stats(input_files) #Precipitation  Annual mm
    #     print("Yearly Average Precipitation: {:.1f} mm".format(result['Yearly_Avg_Precipitation'])) #Precipitation  Annual mm
    #     print("Year with Max Precipitation: {} ({} mm)".format(result['Max_Precipitation_Year'], result['Max_Precipitation_Value'])) #Precipitation  Annual mm
    #     print("Year with Min Precipitation: {} ({} mm)".format(result['Min_Precipitation_Year'], result['Min_Precipitation_Value'])) #Precipitation  Annual mm
    #     print("Yearly Precipitation Standard Deviation: {:.2f} mm".format(result['Yearly_Precipitation_Std'])) #Precipitation  Annual mm

    # data = pd.read_csv(input_files)
    # data['WB2M'] = data['WB2M'].round(2)
    # percentiles = [0.4, 2.0, 5.0, 10.0]
    # monthly_results = calculate_monthly_values(data, percentiles)
    # for month, results in monthly_results.items():
    #     print(f"Month {month}:")
    #     for percentile, t2m_value in results['percentiles'].items():
    #         print(f"  {percentile}: [干球温度: {t2m_value:.2f}, 平均重合湿球温度: {results['average_wb2m'].pop(0):.2f}]")
    #
    # data = pd.read_csv(input_files)
    # data['WB2M'] = data['WB2M'].round(1)
    # percentiles = [0.4, 2.0, 5.0, 10.0]
    # monthly_results = calculate_monthly_values_2(data, percentiles)
    # for month, results in monthly_results.items():
    #     print(f"Month {month}:")
    #     for percentile, wb2m_value in results['percentiles'].items():
    #         print(f"  {percentile}: [湿球温度: {wb2m_value:.1f}, 平均重合干球温度: {results['average_t2m'].pop(0):.1f}]")

