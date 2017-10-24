# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:14:04 2017

@author: xss
"""
import datetime
intime=int(raw_input('输入秒数(s) :'))
outtime = datetime.timedelta(seconds=intime)
#print outtime.strftime('%Y-%m-%d %H:%M:%S')
print str(outtime.strftime(' %H %M %S'))

