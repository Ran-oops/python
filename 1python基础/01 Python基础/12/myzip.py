#导入zip压缩模块
import zipfile

''''''
#压缩操作
#打开新建压缩文件 解压文件操作
zp = zipfile.ZipFile('D:\\ziptest.zip','w')

#加密操作
zp.setpassword('123456'.encode())

#将文件或者文件夹添加到压缩文件当中
zp.write('D:\\FeiQ.exe','fq.exe')
zp.write('D:\\format.pdf','my.pdf')
zp.write('D:\\jsq.py','.\\mydir\\jsq.py')




#关闭压缩文件
zp.close()


'''
#解压操作

#打开压缩文件
zp = zipfile.ZipFile('D:\\ziptest.zip','r')

#解压操作(解压所有内容)
#zp.extractall('C:\\Users\\xdl\\Desktop')

#解压指定内容
zp.extract('fq.exe','C:\\Users\\xdl\\Desktop')

#关闭文件
zp.close()
'''

'''
#查看压缩文件信息
zp = zipfile.ZipFile('D:\\ziptest.zip','r')

#获取指定文件的信息
#result = zp.getinfo('fq.exe')
#print(result)

#获取所有信息列表
#result = zp.infolist()
#print(result)

#获取名称列表
#result = zp.namelist()
#print(result)

zp.close()
'''
