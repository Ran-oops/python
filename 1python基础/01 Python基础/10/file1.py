#文件操作 创建文件并且写入内容
'''
#打开或者创建文件，结果为文件io对象
fp = open('mygirl.txt','w')

print(fp)

#写入文件信息
fp.write('肉夹馍，真腻啊，但是我喜欢！')


#关闭文件
fp.close()
'''

#关于open函数
#open(文件名,文件操作模式)
'''
#w模式
open('mygirl.txt','w')#w模式 写模式write  文件不存在时会创建文件，如果文件已存在则会清空文件
'''


'''
#r模式
fp = open('myboy.txt','r') #r模式  读模式read  文件不存在就报错，存在则准备读取文件
result = fp.read()
print(result)
'''

'''
#a模式
fp = open('myboy1.txt','a')#a模式 追加模式 append 文件不存在则新建，文件存在则在文件末尾追加内容
fp.write('两只小蜜蜂啊，飞在花丛中啊，一个飞得高啊一个飞的低啊，高的对低的说：你个low bee啊')
fp.close()
'''

'''
#x模式

fp= open('myboy2.txt','x')#x模式 抑或模式 xor 文件存在则报错，文件 不存在则新建文件
fp.write('我没啥说的！')
fp.close()
'''

'''
#b模式
fp = open('myboy.txt','b') #b模式 二进制模式 binary 辅助模式不能单独使用
result = fp.read()
print(result)
fp.close()
'''
'''
#+模式
fp = open('myboy.txt','w+') #+模式 增强模式plus  也是辅助模式不能单独使用

#写入操作
fp.write('再见！')

#读取操作
result = fp.read()
print(result)
fp.close()
'''

'''
#read()
fp = open('myboy.txt','r')
txt = fp.read(2)
print(txt)
fp.close()
'''

#write()
fp = open('myboy.txt','a')
result = fp.write('我家住在黄土高坡')
print(result)
fp.close()


