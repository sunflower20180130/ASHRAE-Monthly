#**************DB MCWB
'''
import pandas as pd
def calculate_avg_overlap_wetbulb(data_file, frequency):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)
    # 将实时干球温度数据按月份分组
    monthly_groups = data.groupby('MO')
    # 存储不同累积发生频率下的平均重合湿球温度和选定的干球温度值
    results = []
    # 循环处理每个月份的数据
    for month, month_data in monthly_groups:
        # 对干球温度进行降序排列
        sorted_temperatures = month_data ['T2M'].sort_values(ascending=False)
        # 计算位置索引值
        total_hours = len(month_data)
        index = int(frequency * total_hours)
        # 取出干球温度值
        selected_temperature = sorted_temperatures.iloc [index]
        # 从原数据中筛选同时发生的湿球温度
        matching_wetbulbs = month_data [month_data ['T2M'] == selected_temperature] ['WB2M']
        # 计算平均重合湿球温度
        avg_matching_wetbulb = matching_wetbulbs.mean()
        results.append((month, round(selected_temperature, 1), round(avg_matching_wetbulb, 1)))
    return results

# 请将下面的路径替换为您的数据文件路径
data_file_path = "Shanghai_updated.csv"
# 计算特定累积发生频率（例如0.4%、2%、5%、10%）
frequencies = [0.004, 0.02, 0.05, 0.1]
for frequency in frequencies:
    results = calculate_avg_overlap_wetbulb(data_file_path, frequency)
    print(f"累积发生频率 {frequency * 100}% 下的结果：")
    for result in results:
        month, selected_temp, avg_wetbulb = result
        print(f" {month}, DB: {selected_temp}, MCWB: {avg_wetbulb}")
        '''
#**************WB MCDB
import pandas as pd


def calculate_avg_overlap_drybulb(data_file, frequency):
    # 读取 CSV 文件
    data = pd.read_csv(data_file)

    # 将实时湿球温度数据按月份分组
    monthly_groups = data.groupby('MO')

    # 存储不同累积发生频率下的平均重合干球温度和选定的湿球温度值
    results = []

    # 循环处理每个月份的数据
    for month, month_data in monthly_groups:
        # 对湿球温度进行降序排列
        sorted_temperatures = month_data ['WB2M'].sort_values(ascending=False)

        # 计算位置索引值
        total_hours = len(month_data)
        index = int(frequency * total_hours)

        # 取出湿球温度值
        selected_temperature = sorted_temperatures.iloc [index]

        # 从原数据中筛选同时发生的干球温度
        matching_drybulbs = month_data [month_data ['WB2M'] == selected_temperature] ['T2M']

        # 计算平均重合干球温度
        avg_matching_drybulb = matching_drybulbs.mean()

        results.append((month, round(selected_temperature, 1), round(avg_matching_drybulb, 1)))

    return results


# 输出结果的函数
def print_results(results, frequency):
    print(f"{frequency * 100}%  选定湿球温度    月份     平均重合干球温度")
    for result in results:
        month, selected_temp, avg_drybulb = result
        print(f"  {month}\t {selected_temp}\t{avg_drybulb}")


# 请将下面的路径替换为您的数据文件路径
data_file_path = "Shanghai_updated.csv"

# 计算特定累积发生频率（例如0.4%、2%、5%、10%）
frequencies = [0.004, 0.02, 0.05, 0.1]

for frequency in frequencies:
    results = calculate_avg_overlap_drybulb(data_file_path, frequency)
    print(f"累积发生频率 {frequency * 100}% 下的结果：")
    print_results(results, frequency)

