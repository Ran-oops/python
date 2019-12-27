import random
class human:
	#初始化对象魔术方法  刚做出对象的时候触发，为对象添加成员
	def __init__(self,xingming):
		print('init方法被触发')
		self.name=xingming
		if random.randrange(0,2)==1:
			self.sex='男人'
		else:
			self.sex='女人'
		self.age=28

	def say(self):
		print('你的益达,不，是你的益达')
	def cry(self):
		print('我的律师考试有没有通过！')
zw=human('张益达')
print(zw.age)
print(human.__dict__)
print(zw.__dict__)
