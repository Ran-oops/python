#人类
class human:
	name='美丽的姑娘'
	age=18
	hair=20
	sex='woman'

	def eat(self):
		print('棒棒糖真好吃～')
	def drink(self):
		print('菌子汤中有添加鱼么？味道很鲜美')
	
	def __bool__(self):
		print('bool方法被触发')
		if self.sex=='man':
			return True
		else:
			return False
		
ll=human()
print(ll)
result=bool(ll)
print(result)
