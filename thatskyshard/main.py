import datetime
import date_identify_run  # 导入之前的模块来判断日期是 sharp_before 还是 sharp_after
import sharp_time  # 导入上一个文件来获取时间段

# 定义数据
data = [
    ["云野", "蝴蝶平原", "云中仙乡", "浮岛", "  幽光山洞", "  圣岛"],
    ["雨林", "荧光森林", "密林遗迹", "大树屋", " 后花园", "  秘密花园"],
    ["霞谷", "滑冰场", " 滑冰场", "  圆梦村", "   圆梦村", "    雪隐峰"],
    ["暮土", "边陲荒漠", "远古战场", "黑水港湾", "巨兽荒原", "失落方舟"],
    ["禁阁", "星光沙漠", "星光沙漠", "水母港湾", "水母港湾", "水母港湾"],
]

# 定义表头
headers = ["地图", "周二", "周三", "周五", "周六", "周日"]

# 定义生成地图名称和时间段的函数
def generate_map_schedule(date_input):
    # 调用 date_identify_run.py 中的 check_date 函数
    result = date_identify_run.check_date(date_input)

    # 判断日期是否为 sharp_before 或 sharp_after
    if result not in ["sharp_before", "sharp_after"]:
        return "没有碎片喷发"
    
    try:
        # 获取输入日期的星期几
        date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        day_of_week = date_obj.weekday()  # 获取 (0=周一, 6=周日)

        # 生成星期数
        weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        weekday_name = weekdays[day_of_week]

        # 生成地图名称：1号是暮土，2号是禁阁，3号是云野，4号是雨林，5号是霞谷，6号起循环
        day_of_month = date_obj.day
        map_names = ["暮土", "禁阁", "云野", "雨林", "霞谷"]
        map_name = map_names[(day_of_month - 1) % 5]  # 循环生成地图名称

        # 获取时间段
        time_slot = sharp_time.generate_time_slot(date_input)

        # 生成纯文本表格
        table = f"{'地图':<6}{'星期二':<8}{'星期三':<8}{' 星期五':<8}{'   星期六':<8}{'    星期日':<8}\n"
        table += "-" * 60 + "\n"  # 添加分隔线
        for row in data:
            table += f"{row[0]:<6}{row[1]:<8}{row[2]:<8}{row[3]:<8}{row[4]:<8}{row[5]:<8}\n"

        return f"日期: {date_input}\n时间段: {time_slot}\n地图: {map_name}\n{table}\n生成结果由机器演算，最后更新2024-11-21\nOLSupport@gmail.com"
    
    except ValueError:
        return "错误：日期格式应该为 YYYY-MM-DD"

if __name__ == "__main__":
    # 输入日期
    input_date = input("光遇网易服碎片喷发接口，由OLSupport提供，请输入日期 (YYYY-MM-DD): ")
    result = generate_map_schedule(input_date)  # 获取地图名称、时间段和颜色
    print(result)
    input("Press Any Key Enter to exit...")  # 这行代码会运行结束后暂停，直到你按下回车
