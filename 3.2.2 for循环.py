for 循环语句

for anElement in object:
    #缩进语句块 循环体

    依次遍历对象 (object)中的每个元素，并赋值给anElenment，
然后执行循环体内语句


---------------------------------------
计算 1+2+3+...+10 的值
s = 0
for i in range(11):
    s +=i

print   'sum is :',s


range 函数生成0，1，。。。，10 的序列

------------------------------------
s = 0
i = 1

while i <= 10:
    s += i
    i += 1

print 'sum is ',s
-----------------------------------------
range   函数

range (star,stop[,step])
       起始，终止 ，步长
       i,j,m
       开始值i
       终止值j-1

       [i,j)
       步长可以省略
生成一系列整数
等差数列。。。。

例子

range(2,10)  [2,3,4,5,6,7,8,9]
range(2,10,3)  [2,5,8]
range(10,2,-1) [10,9,8,7,6,5,4,3]
---------------------------------------
求常数e
       1   1    1    1    1    1          1
e=1 + —— + —— + —— + —— + —— + —— + ... + ——
       1！  2！  3！  4！  5！   6！        i！

求一个数的阶乘
import math
e = 1
for i in (1,100):
    e += 1.0/math.factorial(i)  #math.factorial(i) 求阶乘
#1.是因为浮点数精度高，否则整数/整数还是整数 orz

print 'e is ',e


# 第二种方法
#i 的阶乘 相当于 i-1 的阶乘 * i
e = 1
factorial = 1

for i in range(1,100):
    factorial *=1
    e += 1.0 / factorial
print 'e is', e
---------------------------------------------------------------
求常数 π
           1    1     1   1    1        (-1)(i+¹)#这里是（i+1）次方
π = 4（1 - —— + —— - —— + —— - —— +...+ ————    )
           3    5    7    9    11        2i-1


pi = 0
for i in range(1,100):
    pi += (-1.0)**(i+1) / (2*i-1)
pi *=4
print 'pi is ', p


pi = 0
sign = 1
divisor = 1

for i in range(1,1000000):
    pi += 4.0 * sign /divisor
    sign *= -1
    divisor += 2
print 'pi is ', pi


--------------------------------------------
测验
max = 10
sum = 0
extra = 0

for num in range(1, max):
    if num % 2 and not num % 3:
        sum += num
    else:
        extra += 1
print sum

# 余2 为真 and  （not 余3）为真
# 余2为真 and 余3为假
# 左边 1,3,5,7,9 均满足  右边 3,6,9 满足
# 交集为 3，9
# num += sum
# 3+9 =12

有多少个三位数字能被17整除？

num = 0

for i in range(100,1000):
    if (i%17==0):
        num += 1
print num

结果为 53




max = 10
sum = 0
extra = 0

for num in range(1, max):
    if num % 2 and not num % 3:
        sum += num
    else:
        extra += 1
print extra

-------------------------------------------------

冰雹猜想(序列)
考拉兹猜想(英语：Collatz conjecture)
又称奇偶归一猜想 3n + 1 猜想 冰雹猜想 角谷猜想 哈塞猜想 乌拉姆猜想 或叙拉古猜想

对于每一个正整数，如果他是奇数 对他乘3 在加一 如果他是偶数 则对他除以2 如此循环最终都能够得到1

如
n=6  得出序列 6,3,10,5,16,8,4,2,1


n = 6

while n != 1 :
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n +1
    print n,



嵌套循环
打乘法表

----------------------------------------------
for i in range (1,10):
    for j in range (1,10):
        print format(i * j, '3d'),#format 函数 格式化 每个输出占三个整数位 右对齐2333
    print #第一个循环后，打印一个回车让结果更漂亮



输出 99乘法表的左下部分
for i in range(1,10):
    for j in range(1,10):
        if i >= j:
            print format(i * j, '3'),
    print
-------------------------------------------------------------
鸡兔同笼
今有雉兔同笼，上有35头 下有就十四足，问雉兔几何？


穷举法
for chickens in range(35+1):
    for rabbits in range(35+1):
        if 2 * chickens + 4 * rabbits ==94 and chickens + rabbits == 35:
            print chickens,rabbits

while 循环更通用
 任何 for 循环的程序都能用 while 循环实现
 适用场景
    for 已知循环的范围(range)，即起止值和步长

while循环
其他情况 如不确定循环何时终止



-------------------------------------------------------------------------

下列程序一定会进入死循环：

while True:
    for x in range(6):
        y = 2 * x + 1
        if y > 9:
            break
#break 结束当前循环体 并不能终止 while 循环
此论断正确么？“凡是使用 while 循环实现的程序，都能用 for 循环改写。”
# 搞反了 while 次数不确定 可以改写有限次数的 for for 不能改写无限次数的while
