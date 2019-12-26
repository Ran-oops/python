
#文件写入操作
'''
#1.打开或者创建文件
fp = open('1.txt','w')

print(fp)


#2.向文件中写入信息

fp.write('一生一世')

#3.关闭文件
fp.close()
'''


#文件读取操作

#1.打开文件
fp = open('1.txt','r')

print(fp)

#2.读取文件内容
txt = fp.read()
print(txt)

#3.关闭打开的文件
fp.close()
