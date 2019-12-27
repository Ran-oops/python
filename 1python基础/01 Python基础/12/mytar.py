import tarfile

#压缩解压文件操作

#创建或者打开压缩文件
tp = tarfile.TarFile('D:\\myfile.tar','w')


#添加文件
tp.add('D:\\Program Files\\Youdao\\YoudaoNote\\DocToPDF.exe',arcname = 'dtpdf.exe')
tp.add('D:\\Program Files\\Youdao\\YoudaoNote\\ieext_btn.htm',arcname = 'ie.html')
tp.add('D:\\Program Files\\Youdao\\YoudaoNote\\icudtl.dat',arcname = 'ABC/ic.dat')


#关闭压缩文件
tp.close()



#解压操作

#打开文件
tp = tarfile.TarFile('D:\\myfile.tar','r')

#解压文件 所有
#tp.extractall('C:/Users/xdl/Desktop')

#解压单个文件
tp.extract('ie.html','C:/Users/xdl/Desktop')

#关闭文件
tp.close()
