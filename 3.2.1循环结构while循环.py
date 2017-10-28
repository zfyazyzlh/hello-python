多次求解一元二次方程
a=0,b=1,c=1
a=1,b=2,c=1
a=1,b=3,c=1
a=-1,b=1,c=1
a=-1,b=-1,c=1

程序可以多次计算(输入字符'q')退出程序，输入其他字符则继续执行


while 循环结构
#-------------------------------
while 循环条件:
    缩进语句块(循环体)
其余语句
#--------------------------------
while 循环结构的分析策略
1循环体外设定循环可执行的初始条件
2书写需要重复执行的代码(循环体)
3设定循环条件并在循环体内设定条件改变语句

没有这三个，就陷入死循环

例子：
count = 0

while count<5:
    print 'programming is fun!'
    count +=1


循环示例 1+2+3+。。。+10
s = 0
i = 1

while i<=10:
    s += i
    i += 1
print s



循环结构测验
    下列求100以内所有奇数之和的程序是否正确？
sum = 0
i = 1  #这是基数 比较时候要用它比100比大小
while i < 100:
    if i % 2 != 0:
        sum += i
    i += 2
print sum

下列求100以内所有偶数之和的程序是否正确？
sum = 0
i = 0
while i < 100:
    if i % 2 == 0:
        sum += i
        i += 2
print sum


---------------------------------
多次求解一元二次方程
import  math

ch = ''#初始值为空
while ch != 'q':#停止判定
    a=float(raw_input('输入a :'))
    b=float(raw_input('输入b :'))
    c=float(raw_input('输入c :'))


    if a !=0:
        delta=b**2-4*a*c
        if delta < 0:
            print 'No solution'
        elif delta == 0:
            s=-b/(2*a)
            print 's:',s
        else:
            root=math.sqrt(b**2-4*a*c)
            s1=(-b+root)/(a*2)
            s2=(-b-root)/(a*2)
            print 'Two dis tionct solutions are:''{:.2f}'.format(s2) ,'{:.2f}'.format(s1)
    #程序本体缩进到循环体系中
    #并在最后加入是否重复的判定
    ch = raw_input('Quit?')



-------------------------------------------
count = 0

while count < 5:
    if count > 2:
        break
    print 'Programming is fun!'
    count +=1


break 结束当前循环体
    在循环体内部，只要遇到break 则结束当前的循环体


---------------------------------------------
count = 0

while count <5:
    count += 1
    if count > 2:
        continue
    print 'Programming is fun!'

continue 结束当次循环
    只是结束了这一次循环



----------------------------------------
测验
下列程序的输出结果是？
n = 5
while n > 0:
    n -= 1
    if n < 3:
        break
else:
    print n

print n


-------------------------------------------
下列代码的输出结果是？
num = 9
count = 0

while num > 0:
    if num % 2 == 0:
        num /= 2
    elif num % 3 == 0:
        num /= 3
    else:
        num -= 1
    count += 1#计数作用

print count
