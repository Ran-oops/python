
#导入模块
import os

'''
#getcwd()

dirname = os.getcwd()
print(dirname)
'''


'''
#chdir() 
result = os.chdir('D:/')
print(result)

#新建一个文件
fp = open('1.txt','w')
fp.close()
'''

'''
#listdir()

result = os.listdir('D:\\Program Files\\Youdao\\YoudaoNote')

print(result)

print(len(result))
'''

'''
#mkdir()

result = os.mkdir('huangtu')
print(result)
'''

'''
#rmdir()

result = os.rmdir('D:/gp')
print(result)
'''

'''
#makedirs()
#os.makedirs('D:/a/b/c')
'''

'''
#removedirs()
os.removedirs('D:/a/b/c')
'''

'''
#rename()
#result = os.rename('D:/1.txt','D:/a.txt')
#print(result)

os.rename('D:/c','D:/ccc')
'''

'''
#stat()
result = os.stat('D:/a.txt')
print(result)
'''

'''
#system()
result = os.system('ping 127.0.0.1 -t')
print(result)
'''



''''''
#putenv()
result = os.putenv('path','C:/123/123/123')
print(result)

#getenv()
result = os.getenv('path')
print(result.split(';'))



#exit()
