class animal:
	pass
class atom:
	pass
class human(animal,atom):

	
	#属性
	sex='male'
	age=18
	name='刚刚'
	def eat(self):
		print('金粒餐，yoxi～')
		print(human.__name__)

hh=human()
#print(human.__doc__)		
#__bases__获取类的继承列表
#print(human.__bases__)

#__name__在类中表示类名称的字符串
#hh.eat()
print(__name__)