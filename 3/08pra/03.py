##自定义异常类（数据不能为负数）
class NEGError(RuntimeError):
	def __init__(self,errmsg,errline):
		self.errmsg=errmsg
		self.errline=errline
	def __str__(self):
		return self.errmsg+self.errline
try:
	num=-99
	if num<0:
		raise NEGError('NEGError:变量的值小于0的','错误的行数为19')
except NEGError as obj:
	print('数据不能为负数')
	print(obj)