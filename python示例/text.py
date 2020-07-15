#!python2
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8');
"""
Spyder Editor
This is a temporary script file.
"""
print   "1+1"
print "2**2"
print 3**3
'''
wufenzhongdao@wfzd:~/Doc$  env /usr/bin/python /home/wufenzhongdao/.vscode/extensions/ms-python.python-2020.6.91350/pythonFiles/lib/python/debugpy/launcher 38293 -- /home/wufenzhongdao/Doc/hello-python/python示例/text.py 
Traceback (most recent call last):
  File "/home/wufenzhongdao/.vscode/extensions/ms-python.python-2020.6.91350/pythonFiles/lib/python/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_trace_dispatch_regular.py", line 396, in __call__
    file_type = py_db.get_file_type(frame, abs_path_real_path_and_base)  # we don't want to debug threading or anything related to pydevd
  File "/home/wufenzhongdao/.vscode/extensions/ms-python.python-2020.6.91350/pythonFiles/lib/python/debugpy/_vendored/pydevd/pydevd.py", line 864, in get_file_type
    if self.dont_trace_external_files(abs_real_path_and_basename[0]):
  File "/home/wufenzhongdao/.vscode/extensions/ms-python.python-2020.6.91350/pythonFiles/lib/python/debugpy/_vendored/pydevd/_pydevd_bundle/pydevd_api.py", line 819, in custom_dont_trace_external_files
    return abs_path.startswith(start_patterns) or abs_path.endswith(end_patterns)
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe7 in position 43: ordinal not in range(128)
'''