#声明类
#自定义类来继承系统的整形类
class myint(int):
	#魔术方法 触发时机：当前对象+另外一个数值的时候触发
	def __add__(self,other):
		return int(self)*2-int(other)*3

	def __sub__(self,other):
		return int(self)*3+int(other)
	def __truediv__(self,other):
		return int(self)/5-int(other) 
	def __mul__(self,other):
		return int(self)/int(other)


one=myint(5)
#result=one+2
#result=one-5
#result=one/2
result=one*5
print(result)