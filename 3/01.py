#描述符 对成员属性的操作进行控制
#描述符的类
class description:
	def __init__(self):
		self.myname='王饼环'

	def __get__(self,obj,cls):
		result=self.myname[0]+'*'+self.myname[2]
		return result
		
	def __set__(self,obj,value):
		self.myname=value
		

	def __delete__(self,obj):
		del self.myname
		
class Email:
	#属性
	#实例化一个描述对象来管理某个成员属性(交接工作)
	username=description()
	password=None
email=Email()
#print(email.username)
#email.username='小美女'

print(email.username)