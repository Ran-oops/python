#文件指针操作

'''
#tell() 获取当前指针的位置

fp = open('4.txt','w')

#tell() 获取当前指针的位置
pos = fp.tell()
print(pos)

#写文件
fp.write('you need cry dear!')

#tell() 获取当前指针的位置
pos = fp.tell()
print(pos)

fp.close()
'''


#seek() 移动指针位置
'''
fp = open('4.txt','r')

#改变指针位置
fp.seek(4)

#读取4个字符
txt = fp.read(6)

print(txt)

fp.close()
'''

'''
fp = open('4.txt','r')

#改变指针位置
fp.seek(4,0)


#读取6个字符
txt = fp.read(6)

print(txt)

fp.close()
'''


 
