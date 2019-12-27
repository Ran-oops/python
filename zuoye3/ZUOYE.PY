import os
os.chdir(r'C:\Users\Acer\Desktop\zuoye3')
print(os.getcwd())
list1=os.listdir(os.getcwd())
print(list1)

while True:
	handle_file=input('请输入接下来的操作：m：创建文件；rm：删除文件；n:修改文件名；e:退出\n')
	if handle_file=='m'：
		mk_file=input('请输入需要创建的文件夹名称\n')
		os.mkdir(mk_file)
		if mk_file in os.listdir(os.getcwd()):
			print('创建成功')
	elif handle_file=='rm':
		rm_file=input('请输入您要删除的文件夹名称：\n')
		if rm_file in os.listdir(os.getcwd()):
			os.rmdir(rm_file)
			if rm_file not in os.listdir(getcwd()):
				print('恭喜您，删除成功！')
		else:
			print('您输入的文件夹不存在！')
	elif handle_file=='n':
		res=input('请输入需要修改的文件：\n')
		if res in os.listdir(getcwd()):
			re=input('请输入需要改成的名字！\n')
			os.rename(res,re)
			if re in os.listdir(os.getcwd()):
				print('修改成功！')
			else:
				print('您输入的文件不存在！')
	elif handle_file=='e':
		exit()
	else:
		print('输入有误，请按提示输入内容，谢谢！')


