'''
#read() 读取文件信息

#打开文件
fp = open('3.txt','r')

#读取文件
#读取所有信息
#info = fp.read()
#print(info)

#读取指定长度的信息（字符个数）
info = fp.read(5)
print(info)


#关闭文件
fp.close()
'''


'''
#write()写入文件操作

fp = open('31.txt','a')

#写入操作
fp.write('内痔外痔混合痔，请用肛泰肚脐贴！')

fp.close()

'''


'''
#readline() 一次读取一行信息

fp = open('32.txt','r')


#txt = fp.readline()
#print(txt,end = '')


#读取到末尾则读取一个空字符串
#txt = fp.readline()
#print(len(txt))


#循环读取所有行数
while True:
    #读取一行信息
    line = fp.readline()
    #判断是否为空字符串
    if len(line) == 0:
        break
    else:
        print(line)
    


fp.close()
'''


'''
#readlines() 将所有行读取到一个列表当中去

fp = open('32.txt','r')

lines = fp.readlines()

print(lines)

fp.close()
'''

'''
#writelines() 将一个序列中的信息写入文件
fp = open('33.txt','w')

lists = [
    '程晓辉同学很低调\n',
    '张胜杨同志很诱人\n',
    '徐广文同志很好学\n',
    '杨惠君同志很可耐\n'
]

fp.writelines(lists)

fp.close()
'''


#truncate() 文件截取操作

fp = open('34.txt','r+')#r+ 打开文件 光标在最开始的位置

#文件截取操作
result = fp.truncate(2)
print(result)

fp.close()

