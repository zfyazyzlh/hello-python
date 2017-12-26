以下程序的输出结果是？

number = 30
if number % 2 == 0:
    print number, 'is even'
elif number % 3 == 0:
    print number, 'is multiple of 3'

A.30 is multiple of 3
B.程序出错
C.30 is even #√------------------------------------------
D.30 is even
  30 is multiple of 3

以下程序的输出结果是？

x = 1
y = -1
z = 1
if x > 0:
    if y > 0: print 'AAA'
elif z > 0: print 'BBB'

A.语法错误
B.AAA
C.BBB
D.无输出 #√-----------------------------------------

以下程序的输出结果是？

y = 0
for i in range(0, 10, 2):
    y += i
print y

A.9
B.30
C.10
D.20 #√-----------------------------------

如果输入4, -1, 6, 9, 8, 3, 0，请问以下程序的输出结果是？

number = int(raw_input('Enter an integer: '))
max = number
while number != 0:
    number = int(raw_input('Enter an integer: '))
    if number > max:
        max = number
print max

9#----------------------------------

Python语言中，

if x > 0:
    y = 1
else:
    y = -1
等价于：
y = 1 if x > 0 else -1

阅读下面代码，给出x结果：
a = 3
b = 2
x = a if a > b else b

改写回Python

if 3 > 2:
    x = 3
else:
    x = 2

x=3#--------------------------
