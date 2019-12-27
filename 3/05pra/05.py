#人类
class human:
	name='狗蛋'
	sex='nan'
	age=18

	def __new__(cls,color,height):
		print(cls)
		print(color)
		print(height)
		print('new方法被触发')
		#程序制作对象都是objec类中的__new__提供的对象制作功能，我们自己的类都是默认继承object中的
		return object.__new__(cls)
	#测试参数  new魔术方法和init魔术方法的参数必须一只
	def __init__(self,color,height):
		pass
	def say(self):
		print('you are beatiful!')
	def cry(self):
		print('姑娘讨厌我～555～～～')
yzf=human('yellow','185cm')
print(yzf)






















