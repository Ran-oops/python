'''
#人类
class Human:

    #属性
    sex = 'nv'
    age = 38
    length = -12


    #方法
    def say(self):
        print('夏天夏天悄悄过去留下小眯眯')

    def cry(self):
        print('小也不是我的错，都是基因惹的祸')

    #魔术方法   触发时间：对象没有任何变量引用的时候，而不是del变量时候，程序执行完毕会自动回收变量也会触发
    def __del__(self):
        #进行程序的资源回收
        print('del方法被触发')


#实例化对象
wxw = Human()
# print(wxw)

# #将wxw赋值给心的变量
wdw = wxw

# #在这里删除wxw对象
del wxw

print(wdw)
# # #删除wdw变量
# del wdw
#
#
# print('--------------')

'''


#文件读取类
class ReadFile:

    #默认打开文件
    def __init__(self,path):
        self.fp = open(path,'r')

    def readtxt(self):
        txt = self.fp.read()
        print(txt)

    #执行完毕对象自动关闭文件
    def __del__(self):
        print('文件呗关闭')
        self.fp.close()


#实例化对象
file = ReadFile('07.txt')

#读取文件信息
file.readtxt()

