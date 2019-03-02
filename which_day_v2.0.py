"""
    作者:北辰
    功能:输入某年某月某日,判断是这一年的第几天?
    版本:2.0
    日期:18/06/2018
    2.0新增功能:用列表替换元组
"""

from datetime import datetime

def is_leap_year(year):
    """
    判断year是否为闰年
    是,返回true
    否,返回false
    """
    is_leap_year = False
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        is_leap_year = True

    return is_leap_year

def main():
    """
    主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd): ')
    input_date = datetime.strptime(input_date_str,'%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 创建初始的每个月的天数的一个列表
    days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    # 判断闰年
    if is_leap_year(year):
        days_in_month_list[1]=29

    # 计算之前月份的天数总和加上这个月的天数
    days = sum(days_in_month_list[:month-1]) + day

    print('这是{}年的第{}天.'.format(year,days))


if __name__=='__main__':
    main()