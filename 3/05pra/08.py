#人类
class human:
	sex='nan'
	age=18
	def say(self):
		print('洗完澡美美哒～')
	def cry(self):
		print('男朋友不要我啦～')
	def __call__(self):
		print('call被触发')
hh=human()
print(hh)
hh()