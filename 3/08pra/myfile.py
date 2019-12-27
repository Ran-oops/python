#变量
color='green'
#函数
def myfunc():
	print('心如止水')
#类
class human:
	sex='man'
	age=18
	name='hh'
	def say():
		print('这首歌很周杰伦')
	def cry():
		print('对不起，我爱你')

#用于测试的代码
#表示直接运行当前的文件
if __name__=='__main__':
	print('直接运行当前文件')
	print(color)
	human.say()