执行下列语句，输出的结果是？
x = 7.0
y = 5
print x % y
#------------------
2.0
#------------------
能实现下面功能的程序是？
接收用户输入的一个整数。如果输入的是偶数，则输出“True”，否则输出“False”。

A.print not bool(raw_input() % 2)
#程序出错orz
B.print int(raw_input()) % 2 != 0
#偶数输出的是False，不符合
# !=0 变为1 即可
#或者 变为 ==0
C.print int(raw_input()) % 2 == 1
#看上边分析 这个不符合
D.print not bool(int(raw_input()) % 2)
#此程序正确 not 后边跟布尔型（偶数%2） 偶数求余为假 False
#not False 即为True  符合题意

假设你每年初往银行账户中1000元钱，银行的年利率为4.7%。一年后，你的账户余额为：
1000 * ( 1 + 0.047) = 1047 元
#1000 * ( 1 + 0.047)**1
第二年初你又存入1000元，则两年后账户余额为：
(1047 + 1000) * ( 1 + 0.047) = 2143.209 元
#1000*(1+0.047)**2+1000(1+0.047)**1

第三年
[1000*(1+0.047)**2+1000(1+0.047)+1000]*(1+0.047)
#1000*(1+0.047)**3+1000*(1+0.047)**2+1000(1+0.047)
以此类推，第10年年末，你的账户上有多少余额？
1000*(1+0.047)**10+1000*(1+0.047)**9+1000*(1+0.047)**8+1000*(1+0.047)**7+1000*(1+0.047)**6+1000*(1+0.047)**5+1000*(1+0.047)**4+1000*(1+0.047)**3+1000*(1+0.047)**2+1000*(1+0.047)**1=
注：结果保留2位小数（四舍五入）。
print '{:.2f}'.format(1000*(1+0.047)**10+1000*(1+0.047)**9+1000*(1+0.047)**8+1000*(1+0.047)**7+1000*(1+0.047)**6+1000*(1+0.047)**5+1000*(1+0.047)**4+1000*(1+0.047)**3+1000*(1+0.047)**2+1000*(1+0.047)**1)
12986.11

#开始没加入{：.2f} .format限制字符
Python提供了众多的模块。你能找到一个合适的模块，输出今天的日期吗？格式为“yyyy-mm-dd”。可以查找任何搜索引擎和参考资料，并在下面的空白处写出相应的模块名。

#http://www.cnblogs.com/BaiYiShaoNian/p/5084517.html
import datetime

print datetime.date.today()
#+--------
对于一元二次方程，ax²+bx+c=0 若有a-10 b=40 c=15 ，则其解是什么？若有多个解，则按照从小到大的顺序在一行中输出，中间使用空格分隔。解保留2位小数（四舍五入）。
#sqrt(x) 开平方
