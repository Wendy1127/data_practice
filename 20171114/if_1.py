#coding:utf-8
#输入一个星期几，输出他对应的英语名称
#1.设置一个入口，raw_input（下面的条件判断，需要判断字符串）/input（只需判断整数）
weekday=raw_input(u'请输入星期几：')
#2.请使用分支语句做星期判断
if weekday =='1':
    print 'Monday'
elif weekday =='2':
    print 'Tuesday'
elif weekday == '3':
    print  'Wensday'
elif weekday == '4':
    print  'Thursday'
elif weekday == '5':
    print 'Friday'
elif weekday == '6':
    print 'Saturday'
elif weekday == '7':
    print  'Sunday'
else:
    print u'请重新输入：'


