多分支结构(Chained)

将考试分数转换名为等级
例题
分数>=90  打印A
分数>=80  打印B
分数>=70  打印C
分数>=60  打印D
分数<60   打印E

score =78
#gender = 'lady'

if score>=90:
    print 'A'
else:
    if score>=80:
        print 'B'
    else:
        if score>=70:
            print 'C'
        else:
            if score>=60:
                print 'D'
            else:
                if score<60:
                    print 'E'


由于基本if嵌套格式缩进容易出错
所以使用 if elif 语句 达到同样的效果

if score>=90:
    print 'A'
elif score>=80:
    print 'B'
elif score>=70:
    print 'C'
elif score>=60:
    print 'D'
else:
    print 'E'

例题
 求解二元一次方程
 示例文件夹 下
