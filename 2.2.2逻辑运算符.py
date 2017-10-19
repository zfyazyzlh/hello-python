逻辑运算符 Logical Operators

逻辑现实中的体现
    班级里有没有身高一米九以上的男生             1.9+  and  man
    地铁里禁止喝水吃东西                        喝    or   吃
    ...

关系运算符
and     与(全真才真)        True and False == False
or      或(全假才假)        True or False == True
not     非(真变假，假变真)   not True  ==   False

判断一个年份是不是闰年
如果年份y能被4整出但不能被100整除 或者被400整出 则是闰年
    (y%4==0 and y%100!=0) or (y%400==0)

        not (x or y)
        x or y 表示x 或者 y
        not (x or y)表示 不是x 不是y
        not x and not y

    123 and 456
    123 and 456 表示 123 与 456
    # x and y 的值只可能是x或y.  x为真就是y, x为假就是x
    # x or y 的值只可能是x或y.  x为真就是x, x为假就是y
    # and优先级大于or
    非零为真 True

    # python中 and 和 or 运算的核心思想 ——— 短路逻辑
    # http://www.cnblogs.com/an9wer/p/5475551.html
