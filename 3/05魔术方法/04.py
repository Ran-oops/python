import random
#人类
class Human:
    #成员属性（没有在类中设置成员属性，都加到对象中了）

    #成员方法

    #初始化对象魔术方法  刚作出对象的时候触发  作用：为对象添加成员
    def __init__(self,xingming,nianling):
        print('init方法被触发')
        #初始化名字
        self.name = xingming
        #初始化随机分配性别
        if random.randrange(0,2) == 1:
            self.sex = '男人'
        else:
            self.sex = '女人'

        #初始化年龄
        self.age = nianling


    def say(self):
        print('你的益达,不，是你的益达')

    def cry(self):
        print('我的律师考试有没有通过！')


#实例化对象
zw = Human('张益达',28)
print(Human.__dict__)
print(zw.__dict__)

#实例化对象
wxw = Human('伟哥',2)
print(Human.__dict__)
print(wxw.__dict__)