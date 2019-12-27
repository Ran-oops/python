#被别人继承的类--->父类/超类/基类
class liubei:
	familyname='刘'
	firstname='备'
	money='蜀国'
	sex='男'
	__wife='孙尚香，靡夫人'
	age=48

	def say():
		print('各位爱卿，有何良策？')
	def cry():
		print('你这个小畜生，竟然险损我一员大將')
	def makeshoes():
		print('我的草鞋，时尚时尚最时尚～')
	def fire(self):
		print('打死你个龟孙！')

class liuchan(liubei):
	weight=180
	height=167
	fistname='禅'

	def xiangle():
		print('我爸爸是刘备！')
	def cry():
		print('55555！~~~')
	def say():
		#调用父类的say方法
		liubei.say()
		#子类say方法说的话
		print('爸爸，我妈去哪里了')

	def fire(self):
		#1.父类中的fire方法执行一边
		liubei.fire(self)
		#子类的操作			
		print('打死你个鳖肚子！')

#查看liuchan类是否有liubei类
#print(liuchan.__dict__)
#print(liubei.__dict__)
#print(liuchan.age)
#print(liuchan.sex)
#liuchan.say()
#liuchan.cry()
lc=liuchan()
lc.fire()