#描述符2
class Email:
	username=None
	password=None
	def __init__(self):
		self.myname='花花'
	def getusername(self):
		result=self.myname[0]+'*'+self.myname[-1]
		return result
		pass
	def setusername(self,value):
		self.myname=value
		pass
	def delusername(self):
		del self.myname
		pass
	username=property(getusername,setusername,delusername)
email=Email()
#email.username='名米'
del email.username
print(email.username)