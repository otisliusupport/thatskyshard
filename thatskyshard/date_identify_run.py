# file2.py
import datetime

def check_date(date_input):
    try:
        # 将输入转换为日期对象
        date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        day_of_week = date_obj.weekday()  # 获取 (0=周一, 6=周日)

        # 日期判断条件
        if date_obj.day <= 15:
            if day_of_week in [1, 5, 6]:  # 周二、周六、周日
                return "sharp_before"
        else:
            if day_of_week in [2, 4, 5]:  # 周三、周五、周六
                return "sharp_after"

        return "no_sharp"
    except ValueError:
        return "Error_date01 请使用 年年年年-月月-日日 格式"
