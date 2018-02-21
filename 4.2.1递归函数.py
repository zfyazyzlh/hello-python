递归函数

递归：程序调用自身

    形式：在函数定义有直接或间接调用自身


阶乘

 N！= 1*2*3*...*N

 def p(n):
     x = 1
     i = 1
     while i<= n:
         x = x * i
         i = i + 1

    return x

------------------------------
N！= 1*2*3*...*N
↓
N! = (N - 1)! * n

p(n) = p(n-1) * n
↓
(N-1)! = (N-2)! * (N-1)
p(n-1) = p(n-2) * (N-1)

递归 求阶乘

def p(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * p(n-1)

---------------------------------------
def p(n):
    if n == 1 or n == 0:   #初始条件
        return 1           #初始条件
    else:                  '''递归部分'''
        return n * p(n-1)  '''递归部分'''

掐头去尾留中间



递归解决问题的思想
    if 问题足够简单
        直接解决问题
        返回解

    else:
        将问题分解为与元问题同结构的一个或者多个小问题
        逐个解决这些更小的问题
        将结果组合为，获得最终的解
        返回解



小兔子 一个月变为大兔子
大兔子一个月生一对小兔子
第三个月 大兔子生一对小兔子 小兔子变成大兔子

递归 出一共有多少兔子 /月

def fub(n):
    if n ==1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


汉诺塔 移动

def hanoi(n,A,B,C):
    if n == 1:
        print 'Move',n,A,'to',C
    else:
        hanoi(n-1,A,C,B)
        print 'Move',n,'from',A,'to',C
        hanoi(n - 1,B,C,A)

hanoi(2,'左'，'中'，'右')
1111111
