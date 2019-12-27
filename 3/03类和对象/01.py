import time
'''
#clock() python中用于计时的函数(在linux版本中不计算睡眠时间，win中计算睡眠时间) 不提倡使用clock（）

#程序开始之前的计时
start = time.clock()
print(start)

#执行程序
time.sleep(3)

#程序结束之后的计时
end = time.clock()
print(end)

#计算程序执行时间
result = end - start
print(result)

print('程序执行了'+str(result)+'秒')
'''

'''
#perf_counter() 用于计算程序时间的计时器
#程序开始之前的计时
start = time.perf_counter()
print(start)

#执行程序
time.sleep(5)

#程序结束之后的计时
end = time.perf_counter()
print(end)

#计算程序执行时间
result = end - start
print(result)

print('程序执行了'+str(result)+'秒')

'''

'''
#time() 获取当前的本地的时间戳

result = time.time()
print(result)

print(time.ctime(result))
'''

#strftime() 输出格式化之后的时间

tp = (1999,12,23,1,0,0,0,0,0)

result = time.strftime('%m月%d日%Y年  %I:%M:%S %p',tp)

print(result)


#strptime() 将格式化之后的时间提取乘元祖

str1 = '2017/09/6 12:23:45'

result = time.strptime(str1,'%Y/%m/%d %H:%M:%S')

print(result)