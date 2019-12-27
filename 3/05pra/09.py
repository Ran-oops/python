class docake:
	def hm(self):
		print('和面')
	def fj(self):
		print('发酵')
	def hk(self):
		print('烘烤')
	def qxz(self):
		print('切形状')
	def mny(self):
		print('抹奶油')
	def fsg(self):
		print('放水果')
	def bz(self):
		print('包装')
		return '做好的蛋糕'
	def __call__(self):
		self.hm()
		self.fj()
		self.hk()
        self.qxz()
        self.mny()
        self.fsg()
        result=dk.bz()
        return result
dk=docake()
result=dk()
print(result)
