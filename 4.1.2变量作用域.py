变量作用域

globalVar = 1
def f1():
    localVar = 2
    print globalVar
    print localVar

f1()
print globalVar
print localVar
""" 报错localVar没有被定义"""


局部变量
    只能在程序的特定部分使用的变量
    函数内部

全局变量
    为整个程序所使用的变量
    所有函数均可使用

要想在函数内部对函数外面的全局变量进行修改的话，就需要用到global 这个关键词

global x

就表明x不是一个局部变量而是一个全局变量

x = 1

def fun():
    x = 2

fun()
print x


x = 1

def fun():
    global x
    x = x + 1
    print x
fun()
print x



下列程序的执行结果是？

x = 1

def fun(x):
    global x
    x = 2

fun(x)

print x


D.
程序出错
SyntaxError: name 'x' is local and global
 '''参数x 跟变量重复 导致错误'''

函数实现回文素数



num = 151


if is_palin(num) and is_prime(num):
    print 'ok'
else:
    print 'no'



----------------------------
num = 131


is_palin = False
is_prime = False
def is_palin(num):
    num_temp = num
    num_prime = 0
    while num_temp != 0:
        num_prime = num_prime * 10 + num_temp % 10
        num_temp /= 10

    if num == num_prime:
        return True
    else:
        return False

def is_prime(num):
    import math
    for i in range (2,int(math.sqrt(num)+1)):

        if num % i == 0 :
            return False
    return True


if is_palin(num) and is_prime(num):
    print 'ok'
else:
    print 'no'
----------------------------------------------------------

函数的优点
    代码可重用
        提升开发效率
        减少重复编码

    代码更简洁
        函数功能相对独立，功能单一
        结构清晰，可读性好。

    编程更容易把握
        复杂程序分解成较小部件

    封装与信息隐藏



定义如下的函数，下面哪种函数调用会出错 ？

def defaultParameters(arg1, arg2=2, arg3=3):
    print arg1, arg2, arg3


defaultParameters(arg2=10, arg3=10)

缺省参数 arg1 没赋值所以出错

下列程序的输出结果是：

sum = 0
def sum(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i
    return result
print sum(1, 10)
