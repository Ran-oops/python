#单例设计模式
#一个类中只能实例化一个对象
class yuzhenfeng:
	#类中添加一个属性  记录是否创建对象
	obj=None
	#魔术方法 new 控制对象的创建
	def __new__(cls):
		#检测对象是否创建
		if cls.obj==None:
			cls.obj=object.__new__(cls)
			return cls.obj
		else:
			#不是第一次创建对象 直接返回类中存储的那个第一次创建的对象
			return cls.obj
one=yuzhenfeng()
print(one)
two=yuzhenfeng()
print(two)
three=yuzhenfeng()
print(three)
four=yuzhenfeng()
print(four)