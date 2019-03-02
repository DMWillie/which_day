"""
    作者:北辰
    功能:输入某年某月某日,判断是这一年的第几天?
    版本:1.0
    日期:15/06/2018
"""

from datetime import datetime

def main():
    """
    主函数
    """
    input_date_str = input('请输入日期(yyyy/mm/dd): ')
    input_date = datetime.strptime(input_date_str,'%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 创建初始的每个月的天数的一个元组
    days_in_month_tup = (31,28,31,30,31,30,31,31,30,31,30,31)
    # 计算之前月份的天数总和加上这个月的天数
    days = sum(days_in_month_tup[:month-1])+ + day

    if ((year%4==0) and (year%100!=0)) or (year%400==0):
        if month > 2:
            days += 1
    print('这是{}年的第{}天.'.format(year,days))


if __name__=='__main__':
    main()