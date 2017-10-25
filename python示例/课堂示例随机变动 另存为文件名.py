# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:14:04 2017

@author: xss
"""
import  math
#print dir(math)
#print help (math.cosh)
#print help math
a=3 #int(raw_input('输入a :'))
b=4 #int(raw_input('输入b :'))
c=5 #int(raw_input('输入c :'))
cosc=(a**2+b**2-c**2)/(2*a*b)
print float(math.acos(cosc)/math.pi)*180
