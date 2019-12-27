#声明类
class myint(int):
	#魔术方法 触发时间：两个数据进行相等比较的时候触发
	def __eq__(self,other):
		#只要%10余数相等就相等
		result=(int(self)%10==int(other)%10)
		return result
no1=myint(53)
no2=myint(56)
result=(no1==no2)
print(result)

