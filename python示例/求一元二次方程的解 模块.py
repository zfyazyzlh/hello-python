二元一次方程解
#
#sqrt(x) 开平方
#Δ>0 有两个解
#Δ=0 有一个解
#Δ<0 无解
import  math

a=float(raw_input('输入a :'))
b=float(raw_input('输入b :'))
c=float(raw_input('输入c :'))
root=math.sqrt(b**2-4*a*c)

if a !=0:

    if root>0:
        x1=(-b+root)/(a*2)
        x2=(-b-root)/(a*2)
        print '{:.2f}'.format(x2) ,'{:.2f}'.format(x1)
    elif root=0:
        x=(-b+root)/(a*2)
        print '{:.2f}'.format(x)
    else:
        print 'no solution'
