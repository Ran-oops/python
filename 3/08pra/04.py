#原始操作
fp=open('1.txt','w')
fp.write('本草纲目')
fp.close()


#读取文件
#with语法  监控文件的使用状态，在适当的时候自动关闭
try:
	with open('2.txt','r') as fp:
		print(fp.read())
except:
	print('文件打开出错！')

	
