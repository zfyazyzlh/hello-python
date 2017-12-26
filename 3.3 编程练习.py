二分法求平方根

基本思想
猜测一个平方根 x/2
如果猜小了，则正确的平方根在猜测数字和原数之间
如果猜大了，则正确的平方根在0和猜测数字之间

----------------------------------------------
例题：

用二分法猜1到100之间的一个数，最多需要猜多少次？
2*2*2*2*2*2*2=128
2**7=128

---------------------------------------------------
input:X
output:√x
low=0,high=x
guess =(low + high ) / 2

如果 guess² == x,则输出guess，程序结束
如果 guess² < x ， 则low = guess ；继续执行步骤2
如果 guess² > x ， 则 high = guess ； 继续执行步骤2

x =float(raw_input('enter the number'))

low=0
high = x
guess = (low + high )/2
while abs(guess**2 - x) >1e-5 :#绝对值，给定精度  以求得结果

    if guess ** 2 < x:
        low = guess
    else:
        high = guess

    guess = (low + high )/2

print guess


上述不完美，如果输入的数值1>x>0
结果出错
改进方法
-----------------------------------------------------------
x =float(raw_input('enter the number '))

low=0
num = 0

if x<0:
    print '输入的值为负数，本程序不考虑'
else:
    while 0<x<1 :
        x *= 100
        num += 1  #这里先把x扩大一百倍 用num 计数 最后结果 /10的num次方求结果的正确性
    high = x
    guess = (low + high )/2
    while abs(guess**2 - x) >1e-5 : #绝对值，给定精度  以求得结果

        if guess ** 2 < x:
            low = guess
        else:
            high = guess

        guess = (low + high )/2

    print guess/10**num



------------------------------------------
x = float(raw_input("输入x:求x平方根  "))

if x<0:
    print "error"
elif x<1:
    low = x
    high = 1#小数的平方根不小于1但是大于它本身
else:
    low =0.0
    high =x
guess =(low + high)/2

while abs(guess**2-x)>1e-5:

    if guess**2>x:
        high =guess
    else:
        low = guess
    guess = (low + high)/2
print guess

#这个方法出自于 讨论区
#http://mooc.study.163.com/learn/1000002017?tid=2001354013#/learn/content?type=detail&id=2001640347&cid=2001633804
#@思无邪ykt1502277879105 同学 很厉害

-----------------------------------------


判断一个数是不是素数

素数(质数)
一个大于1 的自然数除了1和他本身外，不能被其他自然数整除；否则称为合数。
import math
x = 13
#number = 0
for i in range (2,int(math.sqrt(x)+1)):#终止值为开方 缩短计算步骤

    #number +=1 计算次数计数器
    if x % i == 0 :
         print 'x is not a prime!'
         #print number
         break
else:
    print 'the number is a prime'
    #print number
--------------------------------------
前50个素数
给出的结果有一个问题就是从零开始而不是从而二开始 这个数字1到底算不算 素数
import math
x =0  #教程给出来的是从2开始我们这里可以改成1 后面先加1从2开始算
number = 0
while number <50:
    x+=1
    for i in range (2,int(math.sqrt(x)+1)):#终止值为开方 缩短计算步骤

        #number +=1 计算次数计数器
        if x % i == 0 :
             #print 'x is not a prime!'
             #print number
             break
    else:
        number +=1
        print x,'  ',#,'is a prime','NO.',number


------------------------------------------------------
判断一个数是不是回文数
判断一个数num是否为回文数
求num的逆序num'
如果 num == num' 则num为回文数
否则 num 不是回文数
自己的写法：

num = 12332#int(raw_input('enter the number:'))
num_mun = 0
x = num
while num>10:
    num_mun += (num % 10)
    num_mun *= 10
    num /= 10

num_mun += num

if num_mun == x:
    print x ,'is a 回文数'
else:
    print x,'不是一个回文数'


课程写法

num=int(raw_input('enter the number:'))
num_temp = num
num_prime = 0

while num_temp != 0:
    num_prime = num_prime * 10 + num_temp % 10
    num_temp /= 10

if num == num_prime:
    print ' the number ', num, 'is a polindrome'
else:
    print ' the number ', num, 'is not a polindrome'

整合一下 ：
num = int(raw_input('enter the number:'))
num_mun = 0
x = num

while num != 0:
    num_mun = num_mun * 10 + (num % 10)
    num /= 10

if num_mun == x:
    print x ,'is a 回文数'
else:
    print x,'不是一个回文数'


--------------------------------------------
能否判断一个数是否为回文素数

回文数 and 素数
import math
num = int(raw_input('enter the number:'))
for i in range (2,int(math.sqrt(num)+1)):
    if num % i == 0 :
        break

else:#不停止即为素数，然后看是否回文
    num_mun = 0
    x = num

    while num != 0:
        num_mun = num_mun * 10 + (num % 10)
        num /= 10

    if num_mun == x:
        print x ,'is a 回文素数'


--------------------------------------
以下为改进版本 上述版本并不能描述为什么终止程序 那就接下来区别对待
import math

num = int(raw_input('enter the number:'))
num_mun = 0
x = num

for i in range (2,int(math.sqrt(num)+1)):
    if num % i == 0 :
        num_prime = 0
        break

else:
    num_prime == 1#真值用数字表示 为素数


while num != 0:
    num_mun = num_mun * 10 + (num % 10)
    num /= 10

if num_mun == x:
    num_polindrome = 1#真值用数字表示为回文数
else:
    num_polindrome = 0

if num_prime and num_polindrome:
    print x,'是回文素数'
    
elif num_prime == 1:
    if num_polindrome == 0:
        print x,'是一个素数，但不是一个回文数'
elif num_prime == 0:
    if num_polindrome == 1:
        print x,'不是一个素数，但是一个回文数'
    else:
        print x,'不是一个素数，也不是一个回文数'
