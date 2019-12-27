
import time
'''
#clock() python中用于计时的函数（在Linux版本中不计算睡眠时间，win中计算睡眠时间）不提倡使用clock（）
#程序开始之前的计时
start=time.clock()
print(start)

#执行程序
time.sleep(3)
#程序结束之后的计时
end=time.clock()
print(end)
result=end-start
print(result)
print('程序执行了'+str(result)+'秒')
'''
'''
import time
start=time.clock()
time.sleep(2)
end=time.clock()
result=end-start
print('程序执行了'+str(result)+'秒')
'''
'''
#perf_counter()用于计算程序时间的计时器
#程序开始之前的计时
start=time.perf_counter()
print(start)
#执行程序
time.sleep(2)
end=time.perf_counter()
print(end)

result=end-start
print(result)
print('程序执行了'+str(result)+'秒')
'''
'''

#time()获取当前的本地的时间戳
result=time.time()
print(result)

print(time.ctime(result))
'''

#strftime()输出格式化之后的时间
tp=(1996,5,15,14,20,0,0,0,0)
result=time.strftime('%m月%d日%Y年  %H:%M:%S  %p',tp)
print(result)

#strptime()将格式化之后的时间提取出元组
str1='2017年09月16日  18:22:05'
result=time.strptime(str1,'%Y年%m月%d日 %H:%M:%S')
print(result)










