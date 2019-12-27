#装饰器 为成员方法（函数）或类的功能进行扩展的一种格式
'''
#1.普通的方法
def laxi():
	print('噗～')
laxi()
'''
'''
#2.为函数扩展功能，不是装饰器
def zhuangshi(func):
	print('烧香拜佛，祈求一切顺利')
	func()
	print('烧香还愿，感谢佛祖保佑～～')
def laxi():
	print('噌噌～～')
laxi=zhuangshi(laxi)
laxi()
'''
'''
#3.为函数扩展功能
def zhuangshi(func):
	def inner():
		print('烧香拜佛，祈求一切顺利')
		func()
		print('烧香还愿，感谢佛祖保佑～～')
	return inner
def laxi():
	print('噌噌～～')
laxi=zhuangshi(laxi)

laxi()
'''
'''
#4.真正的装饰器语法
def zhuangshi(func):
	def inner():
		print('烧香拜佛，祈求一切顺利')
		func()
		print('烧香还愿，感谢佛祖保佑～～')
	return inner
@zhuangshi #等价于laxi=zhuanshi(laxi)
def laxi():
	print('噗～')
laxi()
'''
'''
#5.带有参数和返回值的函数
def zhuangshi(func):
	def inner(w,n):
		print('烧香拜佛，祈求一切顺利')
		result=func(w,n)
		print('烧香还愿，感谢佛祖保佑～～')
		return result
	return inner
@zhuangshi
def laxi(who,num):
	print(who,'拉了',num,'斤便便～')
	return '屎'
result1=laxi('吴小伟',200)
print(result1)
result2=laxi('米冬涛',0.1)
print(result2)
'''
'''
#6.带有收集参数的函数  装饰器
#定义装饰器的函数
def zhuangshi(func):
	def inner(*w,**n):
		print('烧香拜佛，祈求一切顺利')
		func(*w,**n)
		print('烧香还愿，感谢佛祖保佑～～')
		#return result 
	return inner
@zhuangshi
def laxi(*whos,**nums):
	print('一堆人参与拉屎')
	print('参与集体拉屎的人有：',whos)
	print('分别拉了多少斤:',nums)
	#return'好多屎'
#调用函数
laxi('欢欢','冰冰','露露','文文',hh=1,bb=2,ll=30,ww=4)
'''
'''
#7.装饰器函数
def zhuangshiqi(type):
	def _zhuangshiqi(func):
		def innerla():
			print('脱下裤子，准备拉屎')
			func()
			print('擦屁股，提裤子走人')
	
		def innerchi():
			print('餐前要洗手~')
			func()
			print('吃完之后，擦嘴，剃牙！')
		if type=='la':
			return innerla
		elif type=='chi':
			return innerchi
	return _zhuangshiqi
@zhuangshiqi('la')
def laxi():
	print('噌噌～～')
@zhuangshiqi('chi')
def chishi():
	print('这坨便便太稀了，需要用勺子蒯这吃～')
laxi()
chishi()
'''
'''
#8.使用类作装饰器的参数
#祈福的类
class wish:
	def before():
		print('烧香拜佛，祈求一切顺利')
	def after():
		print('烧香还愿，感谢佛祖保佑～～')
#当前这一层装饰器用于接收参数
def zhuangshiqi(cls):
	def _zhuangshiqi(func):
		def inner():
			cls.before()
			func()
			cls.after()
		return inner
	return _zhuangshiqi 


@zhuangshiqi(wish)
def laxi():
	print('噌噌～～')
laxi()
'''
'''
#9.使用类作为装饰器使用
class zhuangshiqi:
	#魔术方法 接收装饰器的参数
	def __init__(self,arg):
		self.arg=arg
	#一个用于接收基本函数zhuangshiqi
	def __call__(self,func):
		self.func=func
		return self.inner
	def inner(self):
		print('烧香拜佛，祈求一切顺利')
		self.func()
		print('烧香还愿，感谢佛祖保佑～～')
		
@zhuangshiqi(5)		
def laxi():
	print('噌噌～～')
laxi()
'''
'''
#10.为类添加装饰器
objdict={}
#装饰器函数
def zhuangshiqi(cls):
	def inner():
		if 'only' in objdict:
			return objdict['only']
		else:
			obj=cls()
			objdict['only']=obj
			return objdict['only']
	return inner

@zhuangshiqi
class bingbing:
	sex='female'
	age=18
	bf='不认识'
	def say():
		print('老公，你轻点，揉的太疼了！')

one=bingbing()
print(one)
two=bingbing()
print(two)
'''
#11.多装饰器的使用
#装饰器函数1
def zsq1(func):
	def inner():
		print('脱下裤子，准备拉屎')
		func()
		print('提裤子')
	return inner
def zsq2(func):
	def inner():
		print('烧香拜佛，祈求一切顺利')
		func()
		print('烧香还愿，感谢佛祖保佑～～')
	return inner
@zsq2
@zsq1
def laxi():
	print('吃啥拉啥，那就只能吃屎了～')
laxi()







