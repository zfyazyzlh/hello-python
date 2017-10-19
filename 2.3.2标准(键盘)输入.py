标准键盘输入

raw_input 函数
    功能 读取键盘输入，将所有输入作为字符串看待。
    语法  raw_input([prompt])
        [prompt]是提示符最好提供
    举例
        radius = float(raw_input('Radius:'))
        #变量radius =强制转化浮点数（用户输入的变量（提示字符为"radius：半径的意思"））
 程序内容如下
    pi = 3.14
    radius = float(raw_input('Radius:'))
    area = pi*radius**2
    print area
