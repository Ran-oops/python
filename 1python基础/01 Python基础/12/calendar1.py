import calendar

#常用的日历函数
'''
#calendar()获取指定年份的日历
result = calendar.calendar(2017,w=2,l=1,c=6,m=5)
print(result)
'''

'''
#month() 获取指定年月的日历

result = calendar.month(2017,7)
print(result)

'''

'''
#monthcalendar() 获取指定年月的日历矩阵

result = calendar.monthcalendar(2017,7)

print(result)
'''


'''
#isleap()  检测是否是闰年

result = calendar.isleap(2000)
print(result)

'''

'''
#leapdays() 检测指定年份之间的闰年个数

result = calendar.leapdays(2000,2016)

print(result)
'''

'''
#monthrange()  获取一个月的周几开始及当月天数

result = calendar.monthrange(2017,6)

print(result)
'''

'''
#weekday() 计算周几

result = calendar.weekday(2017,7,3)
print(result)
'''


#timegm() 将时间元组转化为时间戳

tp = (2017,7,3,16,47,0,0,0,0)

result = calendar.timegm(tp)

print(result)
