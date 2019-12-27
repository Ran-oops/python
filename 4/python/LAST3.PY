while True:
	while True:
		begin=input('请输入开始值:')
		if begin.isnumeric()==False:
			print('请输入整数，谢谢！')
		else:
			break
	b=int(begin)		
		
	while True:
		end=input('请输入结束值:')
		if end.isnumeric()==False:
			print('请输入整数，谢谢！')
		else:
			break
	e=int(end)	
	i=0
	while b<e:
		print(b,end='')
		i+=1
		if i%8==0:
			print(end='\n')
		b+=1
