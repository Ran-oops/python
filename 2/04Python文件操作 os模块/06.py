#导入os模块
import os

'''
#system() 执行系统命令
#result = os.system('ping 127.0.0.1 ')
result = os.system('shutdown -s -t 600')
print(result)


#getenv() 获取系统环境变量

result = os.getenv('path')
print(result)

#print(result.split(';'))

for i in result.split(';'):
    print(i)
'''

#setenv() 设置系统环境变量(在当前程序中临时修改)

os.putenv('path','d:\\')

#实验操作（不要用getenv获取，拿不到！）
os.system('feiq')




