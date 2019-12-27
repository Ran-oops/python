#多继承的问题
class baba:
	def say(self):
		print('打死你个龟孙')
class mama:
	def say(self):
		print('打死你个兔崽子！')
class son(baba,mama):
	pass

erzi=son()
erzi.say()
