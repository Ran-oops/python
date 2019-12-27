#继承
class father:
	#成员属性
	__sex='man'
	age=41
	wife='围裙妈妈'
	#成员方法
	def say():
		print('孩子，你妈呢？')
	def cry():
		print('老婆你在哪？')
class son(father):
	pass

#检查儿子类
print(son.__dict__)
#访问儿子类的性别
#print(son.sex)
#print(son.age)
#son.say()
