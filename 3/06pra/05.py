class human:
	#属性
	def __init__(self):
		self.name='浪浪'
		self.age=18
		self.sex='man'
	#方法
	pass

	#魔术方法 触发时间：访问成员属性的时候触发（无论属性是否存在）
	def __getattribute__(self,attrname):
		#print(attrname)
		if attrname=='sex':
			return'woman'
		elif attrname=='age':
			return 28
		else:
			return'就不告诉你！'

hh=human()
print(hh.sex)