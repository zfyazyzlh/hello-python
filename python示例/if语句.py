# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:06:17 2017

@author: xss
"""
#基础if 语句
score =78
if score >=60:
    print 'yes'

#if else 语句
score =78
if score>=60:
    print'yes'
else:
    print'no'


#if 嵌套
score =78
gender = 'lady'
    if score>=60:
        if gender=='lady':
            print 'yes'

#if 条件 合成
score =78
gender = 'lady'
if score>=60 and gender=='lady':
    print 'yes'


#多分支的if
score =78
#gender = 'lady'

if score>=90:
    print 'A'
else:
    if score>=80:
        print 'B'
    else:
        if score>=70:
            print 'C'
        else:
            if score>=60:
                print 'D'
            else:
                if score<60:
                    print 'E'

# 由于上述多分支比较复杂可以改写

if score>=90:
    print 'A'
elif score>=80:
    print 'B'
elif score>=70:
    print 'C'
elif score>=60:
    print 'D'
else:
    print 'E'
