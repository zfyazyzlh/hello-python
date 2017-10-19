变量 Variable
计算年份是否闰年

    (y%4==0 and y%100!=0) or (y%400==0)

    y 为变量

用于引用(绑定)对象的标识符
语法
    变量名= 对象(数值、表达式)


计算圆的面积
    pi=3.14
    #内存中生成一个对象值为 3.14 有个变量pi 来指定这个对象
    radius=12.3
    #内存中生成一个对象值为 12.3 有个变量radius 来指定这个对象
    area = pi*radius**2
    #内存中生成对象值为 475.0506 变量area来指定这个对象

    radius=23.4
    #这时候变径radius变为23.4 内存中重新生成了一个对象 23.4 radius 重新指定他
    print area
    #这时候打印出来的是475.0506呢还是一个新的对象？
    #答案是 原来的475.0506 并没有指向新的对象

    # 如果要计算新的圆的面积需要重新指定到新的对象
    area = pi*radius**2
    print area
    #结果为新的圆的面积

增量赋值运算

count =count +1
    简写
        count +=1

标识符
    变量、函数、模块 等的名字

命名规则
    任意长度
    包含数字和字幕
    但是首个必须是字幕或者下划线
    大小写敏感
    标识符不能是关键字

关键字 (保留字)31个

and     del     from    not           while
as      elif    global  or            with
assert  else    if      pass          yield
break   except  import  print         class
exec    in      raise   continue      finally
is      return  def     for           lambda
try



x = 10
print type(x)   整数
x = 10.0
print type(x)   浮点
x = '10.0'
print type(x)   字符串

<type 'int'>
<type 'float'>
<type 'str'>
