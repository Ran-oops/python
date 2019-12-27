#与属性操作相关的魔术方法
class human:
	age=18
	name='伟哥'
	def __init__(self):
		self.sex='man'
	def __getattr__(self,attrname):
		if attrname=='length':
			return'180cm'
		elif attrname=='height':
			return'120cm'
		else:
			return'就不告诉你！'
	def __setattr__(self,attrname,value):
		if attrname=='sex':
			object.__setattr__(self,attrname,value)
		elif attrname=='age':
			object.__setattr__(self,attrname,value)
		else:
			pass

	def __delattr__(self,attrname):
		if attrname=='sex':
			object.__delattr__(self,attrname)
		if attrname=='age':
			pass


weige=human()
del weige.age
print(weige.age)
