#coding:utf-8
import time
#获取当前时间戳（从1970-01-01开始）
print time.time()

#获取当前日期时间（当前时区的日期时间），返回时间元组（tumple time）
print time.localtime(time.time())
#tm_year 年
# tm_mon 月
# tm_mday 日
# tm_hour 时
# tm_min  分
# tm_sec  秒
# tm_wday 一周的第几天(0-6)
# tm_yday 一年中的第几天(1-366)
# tm_isdst 是否是夏令时区

#1.获取格式化时间
print  time.asctime(time.localtime(time.time()))

#2.时间字符串
print time.strftime('%Y年%m月%d日 %H:%M:%S',time.localtime(time.time()))
print time.strftime('%X %x',time.localtime(time.time()))
#%Y 四位数年份 %y两位数年份
#%m 月份 %M分钟
#%d 一个月内第几天
#%H 24进制的时间 %h 12进制的时间
#%S 秒数
#%a 本地简化星期 %A 完整星期
#%b 本地简化月份 %B 完整月份
#%c 相应日期和时间
#%j 一年中的第几天 %p pm与am标识
#%U 当前星期是一年中的第几个星期（1-54）
#%w 星期几（整型）（从周日开始）（0-6） %W  当前星期是一年中第几个（0-53）
#%x 本地相应日期标识  %X 本地相应时间标识
#%Z 时区
