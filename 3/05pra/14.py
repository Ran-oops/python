#人类
class human:
	name='文文'
	sex='nv'
	age=18

	def say():
		print('姚文涛，你真坏！')
	def cry():
		print('文涛，你的狗咬人了！～')
	def __format__(self,flag):
		print(flag)
		result=flag.split('-')
		#对齐
		dq=result[0]
		#长度
		cd=int(result[1])
		#填充符号
		tc=result[2]
		if dq=='center':
			finalname=self.name.center(cd,tc)
		elif dq=='left':
			finalname=self.name.ljust(cd,tc)
		elif dq=='right':
			finalname=self.name.rjust(cd,tc)
		return finalname
ww=human()
print(ww)
str1='姚文涛的小狗颜色真的很黄，{:left-10-@}很喜欢～'
result=str1.format(ww)
print(result)