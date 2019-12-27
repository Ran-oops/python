#多项分支
'''
if 条件表达式:
    python代码
    python代码
    python代码
    ...
elif 条件表达式:
    python代码
    python代码
    python代码
    ...

 条件表达式
    python代码
    python代码
    python代码
    ...
...
    
else:
    python代码
    python代码
    python代码
    ...



'''

'''
week = 6

if week == 1:
    print('今天是周一，我们吃西红柿炒番茄')
elif week == 2:
    print('今天是周二，我们吃马铃薯炖土豆')
elif week == 3:
    print('今天是周三，我们吃老母鸡炖小母鸡')
elif week == 4:
    print('今天是周四，我们吃大米煮小米')
elif week == 5:
    print('今天是周五，我们吃红薯蒸白薯')
else:
    print('今天是周天，饿着！')
'''

'''
#成绩判断1

cj = 100

#满分
if cj == 100:
    print('满分，爱因斯坦在世啊～')

#优秀85 - 99
elif cj >= 85 and cj <= 99:
    print('优秀，哥们学的不错')

#良好 75 - 84
elif cj>=75 and cj <=84:
    print('良好，学的还凑合～')

#及格 60-74
elif cj>=60 and cj <=74:
    print('及格万岁，多一分浪费，少一分犯罪')

#不及格
else:
    print('不及格，你死定了！')

'''


'''
#成绩判断2

cj = 25

#满分
if cj == 100:
    print('满分，爱因斯坦在世啊～')

#优秀85 - 99
elif 85 <= cj <= 99:
    print('优秀，哥们学的不错')

#良好 75 - 84
elif 75 <= cj <=84:
    print('良好，学的还凑合～')

#及格 60-74
elif 60 <= cj <=74:
    print('及格万岁，多一分浪费，少一分犯罪')

#不及格
else:
    print('不及格，你死定了！')
'''


#成绩判断3

cj = 57
#满分
if cj == 100:
    print('满分，爱因斯坦在世啊～')
#优秀
elif cj>=85:
    print('优秀，哥们学的不错')

#良好
elif cj >= 75:
    print('良好，学的还凑合～')

#及格
elif cj >= 60: 
    print('及格万岁，多一分浪费，少一分犯罪')
#不及格
else:
    print('不及格，你死定了！')
