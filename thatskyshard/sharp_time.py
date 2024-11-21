import datetime
import date_identify_run  # 导入之前的模块判断日期是 sharp_before 还是 sharp_after

# 定义生成时间段的函数
def generate_time_slot(date_input):
    # 调用 date_identify_run.py 中的 check_date 函数
    result = date_identify_run.check_date(date_input)

    try:
        # 获取输入日期的星期几
        date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        day_of_week = date_obj.weekday()  # 获取 (0=周一, 6=周日)

        # 生成星期数
        weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        weekday_name = weekdays[day_of_week]

        # 根据星期几生成相应的时间段和颜色
        if result in ["sharp_before", "sharp_after"]:  # 这两个值才生成时间段
            if day_of_week == 1:  # 周二
                time_slot = "09:08~10:00 / 14:08~15:00 / 19:08~20:00"
                sharp_color = "弱（黑石）"
            elif day_of_week == 2:  # 周三
                time_slot = "09:08~10:00 / 15:08~16:00 / 19:08~20:00"
                sharp_color = "弱（黑石）"
            elif day_of_week == 4:  # 周五
                time_slot = "11:08~12:00 / 17:08~18:00 / 23:08~24:00"
                sharp_color = "强（红石）"
            elif day_of_week == 5:  # 周六
                time_slot = "10:08~11:00 / 14:08~15:00 / 22:08~23:00"
                sharp_color = "强（红石）"
            elif day_of_week == 6:  # 周日
                time_slot = "07:08~08:00 / 13:08~14:00 / 19:08~20:00"
                sharp_color = "强（红石）"
            else:
                return "no_sharp"
        else:
            return "no_sharp"

        return f"星期: {weekday_name}, 喷发强度: {sharp_color}, \n时间段: {time_slot}"
    
    except ValueError:
        return "错误：日期格式应该为 YYYY-MM-DD"

if __name__ == "__main__":
    # 输入日期
    input_date = input("请输入日期 (YYYY-MM-DD): ")
    result = generate_time_slot(input_date)  # 获取时间段和颜色
    print(result)
