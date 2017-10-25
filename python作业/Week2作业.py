1编写程序，完成下列题目（1分）
题目内容：
身体质量指数（Body Mass Index，BMI）是根据人的体重和身高计算得出的一个数字，BMI对大多数人来说，是相当可靠的身体肥胖指标，
其计算公式为：BMI=Weight/High²，其中体重单位为公斤，身高单位为米。编写程序，提示用户输入体重和身高的数字，输出BMI。

输入格式:
输入两行数字，第一行为体重（公斤），第二行为身高（米）

输出格式：
相应的BMI值，保留两位小数。注：可以使用 format 函数设置保留的小数位数，使用 help(format) 查看 format 函数的使用方法。

输入样例：
80
1.75

输出样例：
26.12
时间限制：500ms内存限制：32000kb
#----------------------------------------------------
Weight = float(raw_input('输入体重(kg) :'))

High = float(raw_input('输入身高(m) :'))

BMI=Weight/High**2


print '{:.2f}'.format(BMI)
#format 用法http://www.cnblogs.com/dplearning/p/5702008.html
#----------------------------------------------------------


题目内容：
接收用户输入的一个秒数（非负整数），折合成小时、分钟和秒输出。

输入格式:
一个非负整数

输出格式：
将小时、分钟、秒输出到一行，中间使用空格分隔。

输入样例：
70000

输出样例：
19 26 40
# 时间转换为输出 参考https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
时间限制：500ms内存限制：32000kb
intime=int(raw_input('输入秒数(s) :'))
outtime=str(datetime.timedelta(seconds=intime))
# 时间转换为输出 参考https://stackoverflow.com/questions/775049/python-time-seconds-to-hms
#结果为19:26:40
#输出格式为http://www.jb51.net/article/62518.htm 但是不成功

这里使用time 模块 不用上面的datetime模块
import time
intime=int(raw_input('输入秒数(s) :'))
print time.strftime("%H %M %S", time.gmtime(intime))

运行结束 跟题目完全一致
over

你可以在此直接在线输入程序代码。
3编写程序，完成下列题目（2分）
题目内容：
对于三角形，三边长分别为a, b, c，给定a和b之间的夹角C，则有：c²=a²+b²-2*a*b*cos(C)。编写程序，使得输入三角形的边a, b, c，可求得夹角C(角度值)。

输入格式:
三条边a、b、c的长度值，每个值占一行。

输出格式：
夹角C的值，保留1位小数。
c²=a²+b²-2*a*b*cos(C)
(a²+b²-c²)/(2*a*b)=cos(C)


输入样例：
3
4
5

输出样例：
90.0

时间限制：500ms内存限制：32000kb
import  math

a=int(raw_input('输入a :'))
b=int(raw_input('输入b :'))
c=int(raw_input('输入c :'))
cosc=(a**2+b**2-c**2)/(2*a*b)
#题目中cosC=1
#求出弧长转化为角度orz
#http://www.jb51.net/article/66175.htm
print float(math.acos(cosc)/math.pi)*180
