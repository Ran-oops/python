
#writelines()
#打开文件
fp = open('mysleep.txt','w')

#读写文件
result = fp.writelines(['爱情公寓1','爱情公寓2','爱情公寓3','爱情公寓4'])
print(result)

#关闭文件
fp.close()


'''
#readline
#打开文件
fp = open('mysleep.txt','r')

#读写文件
result = fp.readline(6)
print(result)

result = fp.readline()
print(result)


#关闭文件
fp.close()

'''

'''
#readlines()

fp = open('mysleep.txt','r')

result = fp.readlines(6)
print(result)

fp.close()

'''


#truncate()

fp = open('mysleep.txt','a')

result = fp.truncate(111)
print(result)

fp.close()


'''
#tell ()

fp = open('tran.txt','r+')

#获取指针位置
pos1 = fp.tell()
print(pos1)

#读取文件
result = fp.read(5)
print(result)

#再次获取指针位置
pos2 = fp.tell()
print(pos2)


#调整指针的位置
fp.seek(10)

#读取文件
result = fp.read(5)
print(result)

#再次获取指针位置
pos2 = fp.tell()
print(pos2)


fp.close()
'''

'''
fp = open('tran.txt','r+')

#获取当前指针的位置
print(fp.tell())

#调整指针位置
print(fp.seek(16))

#写入
fp.write('皮球')

fp.close()
'''
'''
fp = open('tran.txt','r+')



#调整指针位置
fp.seek(5,1)
#获取当前指针的位置
print(fp.tell())

#读取操作
print(fp.read(1))

fp.close()
'''
