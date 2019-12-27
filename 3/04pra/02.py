#受保护的封装操作
class die:
	familyname='夏'
	_money='100'
	sex='man'
	age=21

	def sing():
		print('大风车呼呼啦~')
	def _run():
		print('臭小子，你给我站住！')

class son(die):
	pass



