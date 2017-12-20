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
