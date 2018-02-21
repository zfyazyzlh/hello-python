程序包括 顺序 选择 循环 三种结构
为什么还要介绍函数的概念

回文素数的问题

1判断回文数
num=int(raw_input('enter the number:'))
num_temp = num
num_prime = 0

while num_temp != 0:
    num_prime = num_prime * 10 + num_temp % 10
    num_temp /= 10

if num == num_prime:
    print  'is a polindrome'
else:
    print  'is not a polindrome'



2判断素数
import math
x = 13

for i in range (2,int(math.sqrt(x)+1)):

    if x % i == 0 :

         break
else:
    print 'the number is a prime'

-------------------------------------------------------

import math
num = 13
num_temp = num
num_prime = 0

is_palin = False
is_prime = False

while num_temp != 0:
    num_prime = num_prime * 10 + num_temp % 10
    num_temp /= 10

if num == num_prime:
    is_palin = True


for i in range (2,int(math.sqrt(x)+1)):

    if num % i == 0 :
         break
else:
    is_prime = True

if is_palin and is_prime:
    print 'ok'
else:
    print 'no'

不直观
---------------------------------------------



函数 更直观
num = 151


if is_palin(num) and is_prime(num):
    print 'ok'
else:
    print 'no'

------------------------------
函数是什么
完成特定功能的一个语句组，这组语句可以作为一个单位使用，并且给他取一个名字
 通过函数名执行
 |函数名| 参数
   ↓     ↓
function(x)=
    x²-2x+1


如： abs(x)#求x的绝对值


定义一个函数的方法：
关键字
 ↓   函数名        参数 形式参数parameter
 ↓      ↓     |  ↓      | ：
def print_sum(start,stop):                   #函数头
    """
    to calculate the sum from start to stop  #这里面包含的是说明文档
    """
    result = 0                               #
    for i in range(start,stop + 1):          #里面为语句
        result += i                          #
    print 'Sum is ',result                   #            函数头+ 说明文档+ 语句 构成函数体


调用函数
    print_sum(1,10)
              |实际参数 实参 argument
                        ↓ #函数调用过程是将实参的值一一对应赋值给形参
               行参 parameter
              |形式参数 |
def print_sum(start,stop):
    result = 0
    for i in range(start,stop + 1):
        result += i
    print 'Sum is ',result


--------------------------------------------------
下列程序的输出结果是？

x = 1

def fun(y):
    y = 2

fun(x)
print x



输出  1

------------------------------------------------
缺省参数
                            赋值
def defaultParameters(arg1,arg2=2,arg3=3):
    print 'arg1',arg1
    print 'arg2',arg2
    print 'arg3',arg3

调用函数时候 值为10 arg2 arg3 是什么呢
defaultParameters(10)




如果实参没有给，就是使用缺省参数对他进行赋值


如果有两个
defaultParameters(10，10)

如果有三个  都给了 就用实参
defaultParameters(10，10，10)






有返回值的函数


def print_sum(start,stop):
    result = 0
    for i in range(start,stop + 1):
        result += i
    return result
   """
   return 的含义是函数调用完之后 进行数据的返回
   函数遇到 return 语句终止当前函数的执行
   return 后的语句将被忽略
   """

-------------------------------------------------------
1
下列程序的输出结果是？

x = 1

def fun(x):
    x = 2

fun(x)
print x

输出 1          ？？？？？？？？？？？？？？？？？这里不太懂

"""如果局部变量和全局变量的名称相同的话，
    那么在函数内部其实是对局部变量进行操作
    并没有对外面的全局变量进行操作    """


下列的说法是否正确：“使用函数一定会提高程序的执行效率。”

X



下列说法是否正确：“使用函数总是可以减少程序的代码”

x
