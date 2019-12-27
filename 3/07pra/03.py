#抽象类
import abc
#完成一个用户操作的类
class user(metaclass=abc.ABCMeta):
	company='禽兽与美女公司'
	year=2018

	def listuser(self):
		print('列举所有用户信息')
	@abc.abstractmethod
	def adduser(self):
		pass
	@abc.abstractstaticmethod
	def setuser():
		pass
	@abc.abstractclassmethod
	def deluser(cls):
		pass
#1.抽象类无法直接使用，也无法进行实例化操作
#2.抽象类只能被其他类继承，然后将其他未完成的方法完成
class hhuser(user):
	def adduser(self):
		print('添加用户操作！')

class bbuser(hhuser):
	@staticmethod
	def setuser():
		print('设置用户操作！')
class wwuser(bbuser):
	@classmethod
	def deluser(cls):
		print('删除用户的操作！')
u=wwuser()
u.adduser()
bbuser.setuser()
wwuser.deluser()
u.listuser()