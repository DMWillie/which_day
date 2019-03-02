"""
    作者:北辰
    功能:输入某年某月某日,判断是这一年的第几天?
    版本:3.0
    日期:18/06/2018
    2.0新增功能:用列表替换元组
    3.0新增功能:将月份划分为不同的集合再操作
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
    # 包含30天的月份集合
    _30_days_month_set = {4,6,9,11}
    # 包含31天的月份集合
    _31_days_month_set = {1,3,5,7,8,10,12}

    # 初始化值
    days = day

    for i in range(1,month):
        if i in _30_days_month_set:
            days+=30
        elif i in _31_days_month_set:
            days+=31
        else:
            days+=28

    # 判断闰年
    if month>2 and is_leap_year(year):
        days+=1
    print('这是{}年的第{}天.'.format(year,days))


if __name__=='__main__':
    main()