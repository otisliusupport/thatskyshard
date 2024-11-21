# file1.py
import date_identify_run  # 导入date_identify_run.py函数

def main():
    input_date = input("请输入日期 (YYYY-MM-DD): ")
    result = date_identify_run.check_date(input_date)  # 调用 date_identify_run.py 中的 check_date 函数
    print(f"结果: {result}")

if __name__ == "__main__":
    main()
