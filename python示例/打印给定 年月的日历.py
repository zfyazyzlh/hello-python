#!python2
# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
def is_leap_year(year):
    """
    判断是否闰年
    """
    if year % 4 == 0 and year %100 != 0 or year % 400 ==0:
        return  True
    else:
        return  False

def get_num_of_days_in_month(year, month):
    """
    判断每月的天数
    """
    if month in (1,3,5,7,8,10,12):
        return  31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28

def get_total_num_of_days(year, month):
    """
    判断一共经历了多少天
    """
    days = 0
    for y in range(1800,year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365

    for m in range(1,month):

        days += get_num_of_days_in_month(year, m)
        # 课件中说明的 get_num_of_days_in_month 参数值为year ，m
        # 实际跑程序时候运行的是month才能run起来
        # debug 发现 月份参数并没有赋值 ，小心orz

    return days

def get_start_day(year, month):
    return (3 + get_total_num_of_days(year,month)) %7

print  get_start_day(2018,1)


'''
-----------------------------------------------------
下列程序的输出结果是：

x = 1
y = 2
def swap(x, y):
    t = x
    x = y
    y = t
    print x, y
swap(x, y)
print x, y


2 1

1 2


---------------------------------
下列程序的输出结果是：

x = 1
y = 2
def swap(a, b):
    t = a
    a = b
    b = t
    print a, b
swap(x, y)
print x, y




2 1

1 2
'''