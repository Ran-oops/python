#永久执行的循环代码就是死循环

'''
#应该避免的死循环操作
num = 0

while num<100:
    print(num)
    #num += 1 #业务逻辑中需要变化，但是你没写
'''



#生成特定的死循环

while True:
    print('我是最帅的讲师！')
