# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:14:04 2017

@author: xss
"""
import  math

a=10 #int(raw_input('输入a :'))
b=40 #int(raw_input('输入b :'))
c=15 #int(raw_input('输入c :'))
deerta=b**2-4*a*c

x1=(-b+math.sqrt(deerta))/(a*2)
x2=(-b-math.sqrt(deerta))/(a*2)     

print '{:.2f}'.format(x2) ,'{:.2f}'.format(x1)