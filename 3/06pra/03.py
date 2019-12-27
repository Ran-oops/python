#描述符3
class Email:
	username=''
	password=''
	def __init__(self):
		self.myname='小冰冰'
	@property#用于声明当前方法名称是一个成员属性
	def username(self):
		result=self.myname[0]+'*'+self.myname[-1]
		return result
	@username.setter
	def username(self,value):
		self.myname=value
	@username.deleter
	def username(self):
		del self.myname
email=Email()
#email.username='小红红'
del email.username
print(email.username)
