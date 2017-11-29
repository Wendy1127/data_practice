#coding:utf-8
import calendar
#打印日历
print calendar.calendar(2017,w=2,c=1)

#calendar(year,w，l,c)  w 代表日期的宽度占多少个字符;l 一个星期所占行数；c 每个月间隔的宽度
#总宽  21*w+2*c  如果3个月为一行
#返回当前起始日期，默认首次载入返回0，即星期日
print calendar.firstweekday()
print calendar.firstweekday()   #返回当前每周起始日期的设置

print calendar.isleap(2017)
print calendar.isleap(2018)
print calendar.isleap(2000)
print calendar.leapdays(2000,2017)  #两个时间内有多少个闰年
print calendar.month(2017,11)   #某个月的日历

print calendar.monthcalendar(2017,11)   #自己拼接日历