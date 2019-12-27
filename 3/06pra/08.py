#声明类
class myint(int):
	def __radd__(self,other):
		return int(self)-int(other)
one=myint(2)
result=3+one
print(result)