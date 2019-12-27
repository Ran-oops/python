#导入模块
import tarfile

'''
#压缩文件方法

#打开或者创建压缩文件
tp = tarfile.open('C:\\Users\\xdl\\Desktop\\py04.tar','w:bz2')


#添加文件
tp.add('D:\\FeiQ.exe','fq.exe')
tp.add('D:\\format.pdf','fm.pdf')
tp.add('D:\\jsq.py','calc\\jsq1.py')


#关闭压缩文件
tp.close()
'''


#解压软件
#打开压缩软件
tp = tarfile.open('C:\\Users\\xdl\\Desktop\\py04.tar','r')

#解压操作
#解压所有文件操作
#tp.extractall('C:\\Users\\xdl\\Desktop\\py04')

#解压单个文件
#tp.extract('fq.exe','C:\\Users\\xdl\\Desktop')

#获取解压列表（解压指定列表）
#获取所有文件列表，分片获取指定解压文件即可
lists = tp.getmembers()
#print(lists)
tp.extractall('C:\\Users\\xdl\\Desktop\\py04',lists[0:2])



#关闭解压软件
tp.close()
