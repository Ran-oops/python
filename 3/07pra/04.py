import abc
#定义规则（抽象类）
class animal(metaclass=abc.ABCMeta):
	#定义叫方法
	@abc.abstractmethod
	def jiao(self):
		pass
	@abc.abstractmethod
	def niao(self):
		pass

class Dog(animal):
	def jiao(self):
		print('汪汪～～')
	
	def niao(self):
		print('抬起后腿尿～～')
class Cat(animal):
	def jiao(self):
		print('喵喵～')
	def niao(self):
		print('蹲着尿～')
class XiaoWei(animal):
	def jiao(self):
		print('呀咩跌')
	def niao(self):
		print('站着尿～')

#行为类
class action:
	obj=None
	@classmethod
	def say(cls):
		cls.obj.jiao()
	@classmethod
	def pee(cls):
		cls.obj.niao()
dog=Dog()
cat=Cat()
xw=XiaoWei()
#将对象传入类中
action.obj=dog
action.say()

