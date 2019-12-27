#多继承
#爷爷类
class yeye:
	def damajiang(self):
		print('四川麻将写真馆～')
class nainai:
	def dapuke(self):
		print('炸金花～')
class laoye:
	def doudizhu(self):
		print('四个二带大小王')
class laolao:
	def dezhoupuke(self):
		print('性感荷官在线发牌～')
class baba(yeye):
	def tuipaijiu(self):
		print('虎头~')
class mama(laolao):
	def yaoshaizi(self):
		print('66666~')
class laowu:
	def yaoweixin(self):
		print('美女，约不～')
class son(laowu,baba,nainai,laoye,mama):
	def duma(self):
		print('11号快点跑！')
erzi=son()
erzi.damajiang()
erzi.dapuke()
erzi.dezhoupuke()
erzi.doudizhu()
erzi.duma()
erzi.tuipaijiu()
erzi.yaoshaizi()
erzi.yaoweixin()