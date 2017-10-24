篮球比赛领先多少才算安全？
bill james 算法

算法描述

获取领先的分数
减去三分
如果领先球队控球 则加0.5 否则减 0.5 (小于0则变成0)
计算平方后的结果
如果得到的结果比当前比赛剩余时间的秒数大，则领先是安全的。

points = int(raw_input('Leading points :'))
#输入领先分数
has_ball = raw_input('The leding team has ball (yes/no)')
#是否领先队伍控球
#大写YES的问题
seconds = int(raw_input('The remaining seconds:'))
#比赛剩余时间
#如果剩余时间是0.5 ？ 小数的问题
win = points - 3
if has_ball == 'yes':
    win += 0.5
else:
    win -= 0.5

if win >=0:
    win=win
else:
    win=0

if win**2 > seconds:
    print '安全'
else :
    print '不安全'
