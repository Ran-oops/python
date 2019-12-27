'''
#人类
class human:
	sex='nv'
	age=28
	length=-12

	def say():
		print('夏天夏天悄悄过去留下小秘密')
	def cry():
		print('小也不是我的错，都是基因惹的祸')
	#魔术方法  触发时间：对象没有任何变量引用的时候，而不是del变量的时候，程序执行完毕会自动回收变量也会触发
	def __del__(self):
		print('del方法被触发')
wxw=human()
print(wxw)
wdw=wxw
del wxw
print(wdw)
print('------')
'''
#文件读取类
class readfile:
	#默认打开文件
	def __init__(self,path):
		self.fp=open(path,'r')
	def readtxt(self):
		txt=self.fp.read()
		print(txt)
	#执行完毕对象之后自动关闭文件
	def __del__(self):
		print('文件被关闭')
		self.fp.close()
file=readfile('07.txt')
file.readtxt()