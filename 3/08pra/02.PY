'''
try:
	尝试执行的python语句
	。。。。。。。
	。。。。。。。
except IndexError：#接收特定异常
    用于接收异常的区域
except KeyError:
except NameError:
except IndentationError:
except:#接收所有异常
	用于接收异常的区域

else:#没有异常的情况
	pass
fianlly:#无论是否出现异常都会执行的区域
	pass
'''
'''
#操作1
try:
	lists=['露露','欢欢','冰冰','文文']
	print(lists[20])
except IndexError:
	print(lists[-1])
'''
'''
#操作2
try:
	dicts={'hh':'欢欢','bb':'冰冰','ww':'文文','ll':'露露'}
	print(dicts['aa'])
except IndexError:
	print('索引不正确')
except NameError:
	print('变量名称不正确')
except KeyError:
	print('对不起，访问键不存在！')
'''
'''
try:
	a=10
	b=20
	c=30
	result=b/0
	print(result)
	print(d)
except IndexError:
	print('索引不正确')
except NameError:
	print('变量名称不正确')
except KeyError:
	print('访问键不存在')
except:
	print('其他异常出现')
else:
	print('报告领导，一切正常')
finally:
	print('领导再见，我下班了！')
'''
try:
	print(ndy)
#except NameError as obj:#obj自定义的变量用于接收
#	print('出现了命名错误！')
#	print(obj)

