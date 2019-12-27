class human:
	@classmethod
	def say(cls):
		print('说话方法')
	@staticmethod
	def cry():
		print('哭泣方法')
	
	#非绑定类方法
	def run(self):
		print('跑步方法')

ll=human()
ll.say()
human.say()
ll.cry()
human.cry()
ll.run()