#人类
class human:
	name='美丽的姑娘'
	age=18
	hair=20

	def eat(self):
		print('棒棒糖真好吃～')
	def drink(self):
		print('菌子汤中有添加鱼么？味道很鲜美')

	#魔术方法  触发时机：使用repr()操作对象的时候
	def __repr__(self):
		pass
		#必须有返回值，必须是字符串
		return '露露是个会学习的姑娘122222！～'
	
ll=human()
#result=repr(ll)
#Bprint(result)
result=str(ll)
#print(result)	