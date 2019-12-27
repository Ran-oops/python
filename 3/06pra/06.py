class human:
	sex='man'
	age=18
	height='180cm'

	def __init__(self):
		self.name='赛亚人'
		self.wife='奥特曼'
	def say(self):
		print('邻家小妹妹')
	def cry(self):
		print('他抢了我的棒棒糖')
	#魔术方法
	def __dir__(self):
		objmembers=self.__dict__.keys()
		clsmembers=human.__dict__.keys()
		lists=[]
		for i in clsmembers:
			if (i.startswith('__') and i.endswith('__'))==False:
				lists.append(i)
		lists+=objmembers
		return lists
sq=human()
#dir()函数 获取一个对象中所有可以访问的成员列表
result=dir(sq)
print(result)
