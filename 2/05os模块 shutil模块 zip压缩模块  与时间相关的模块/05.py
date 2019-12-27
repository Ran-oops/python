#d导入模块
import zipfile


#压缩操作
'''
#打开或者创建zip文件
zp = zipfile.ZipFile('C:\\Users\\xdl\\Desktop\\py04.zip','w',zipfile.ZIP_DEFLATED)


#向压缩文件中添加内容(文件或者目录)
zp.write('D:\\FeiQ.exe','fq.exe')
zp.write('D:\\format.pdf','fm.pdf')
zp.write('D:\\jsq.py','mycalc\\jsq.py')


#关闭zip文件
zp.close()
'''



#解压操作

#打开压缩zip文件
zp = zipfile.ZipFile('C:\\Users\\xdl\\Desktop\\py04.zip','r')


#解压文件
#解压所有文件
#zp.extractall('D:\\test')

#解压指定文件
zp.extractall('D:\\test',['mycalc/jsq.py','fm.pdf'])#注意路径

#解压一个文件
#zp.extract('fq.exe','D:\\test')


#关闭压缩文件
zp.close()
