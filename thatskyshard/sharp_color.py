import datetime  # 导入 datetime 模块
import date_identify_run  # 导入你之前的模块

def get_color_based_on_day(date_input):
    # 调用 date_identify_run.py 中的 check_date 函数
    result = date_identify_run.check_date(date_input)

    if result in ["sharp_before", "sharp_after"]:  # 只有这两个值才做颜色判断
        try:
            # 获取日期对象并解析星期几
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()  # 解析日期
            day_of_week = date_obj.weekday()  # 获取 (0=周一, 6=周日)

            # 判断星期几返回相应颜色
            if day_of_week == 1 or day_of_week == 2:  # 周二（1）或周三（2）
                return "black"
            elif day_of_week in [5, 6, 4]:  # 周六（5）、周日（6）或周五（4）
                return "red"
            else:
                return "no_color"  # 如果不在这些日期范围内，返回 "no_color"
        except ValueError:
            return "Error_date01 请使用 年年年年-月月-日日 格式"
    else:
        return "Invalid date result"

if __name__ == "__main__":
    # 输入日期
    input_date = input("请输入日期 (YYYY-MM-DD): ")
    color = get_color_based_on_day(input_date)  # 获取颜色
    print(f"结果: {color}")
