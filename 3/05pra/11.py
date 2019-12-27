#人类
class human:
	name='美丽的姑娘'
	age=18
	hair=20

	def eat(self):
		print('棒棒糖真好吃～')
	def drink(self):
		print('菌子汤中有添加鱼么？味道很鲜美')
	def __str__(self):
		print('str被触发')
		return '露露是个美丽的姑娘～'

ll=human()
print(ll)

