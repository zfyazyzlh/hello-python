运算符

圆的半径为 3cm ，求圆的面积
    公式为 S= π*R²
            π*3²
    python 中为 3.14*3*3

若三名学生的身高分别为1.65，1.78，1.82 求他们的平均身高
         1.65+1.78+1.82
        _______________
              3

          python中表示为  (1.65+1.78+1.82)/3

算数运算符

+   加法  Addition         10+20=30
-   减法  Subtraction      10-20=20
*   乘法  Multiplication   10*20=5
/   除法  Division         10/2=5
%   求余  Modulus          10%3=1
**  指数  Exponent         2**3=8

将华氏度℉ 转化为 摄氏度℃
        5
    ℃=____(℉-32)
        9
    如果℉=75 对应python 代码
        1：5/9*(75-32) 运行结果为0
        2：5.0/9*(75-32) 运行结果23.88888
        因为
        python 2 中"/"表示 向下取整除 (floor division)
        两个整数相除，结果也是整数 舍去小数部分
        如果有一个为浮点数，则结果为浮点数
        式子1：5/9=0.5555 舍去小数 为 0*(75-32) 结果为零

        #(75-32)5/9 这个式子报错 未知原因

自动类型转换
    若参与运算的两个对象的类型相同，则结果类型不变
        1/2=0
    若参与运算的两个对象的类型不同，则按照以下规则自动类型转换
        bool int float complex
        布尔  整数  浮点  复数

        1.0+3=4.0
        True + 3.0 =4.0
        True 为1     False 为0
        非 0为 真True

求余运算

        10%3=1

若今天是星期六 十天后是星期几
        (6+10)%7=2

判断一个数x是否为偶数
        x%2 是否为0

math 模块
模块 module
实现功能的python 脚本集合
引入模块
    import module_name


math 模块
    import  math
    查看模块内容
        dir(math)
            >>> dir(math)
['__doc__', '__name__', '__package__', 'acos',
 'acosh', 'asin', 'asinh', 'atan', 'atan2',
'atanh', 'ceil', 'copysign', 'cos', 'cosh',
'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1',
 'fabs', 'factorial', 'floor', 'fmod', 'frexp',
  'fsum', 'gamma', 'hypot', 'isinf', 'isnan',
  'ldexp', 'lgamma', 'log', 'log10', 'log1p',
  'modf', 'pi', 'pow', 'radians', 'sin', 'sinh',
   'sqrt', 'tan', 'tanh', 'trunc']
    使用模块
        math.pi
    使用帮助
    help(math.sin)
        sin(...)
        sin(x)

        Return the sine of x (measured in radians).
