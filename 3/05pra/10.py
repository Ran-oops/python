#人类
class human:
	name='美丽的姑娘'
	age=18
	size='36D'
	hair=20

	def __init__(self):
		self.height=180
		self.sex='nv'
	def eat(self):
		print('棒棒糖真好吃～')
	def drink(self):
		print('菌子汤中有添加鱼么？味道很鲜美')
	#魔术方法 触发时机：使用len()检测对象时触发
	def __len__(self):
		result=len(self.__dict__)
		return result
ww=human()
result=len(ww)
print(result)