#水果类
class fruit:
	pass
#按地域划分
#南方水果
class southfruit(fruit):
	pass
class northfruit(fruit):
	pass
#按是否可以送礼
class southgiftfruit(southfruit):
	pass
class southnogiftfruit(southfruit):
	pass
class northgiftfruit(northfruit):
	pass
class northnogiftfruit(northfruit):
	pass

class apple(northgiftfruit):
	pass
class pear(northnogiftfruit):
	pass
class banana(southnogiftfruit):
	pass
class orange(southgiftfruit):
	pass