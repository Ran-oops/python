#声明4个类

#动物类A
class Animal:

    #叫的方法
    def say(self):
        print('Animal类 start')
        print('Animal类 end')

#人类B
class Human(Animal):

    # 叫的方法
    def say(self):
        #人类叫 开始
        print('Human类 start')
        #调用动物类的叫方法
        super().say()
        # 人类叫 开始
        print('Human类 end')


#鸟类C
class Bird(Animal):
    # 叫的方法
    def say(self):
        # 鸟类叫 开始
        print('Bird类 start')
        # 调用动物类的叫方法
        super().say()
        # 鸟类叫 开始
        print('Bird类 end')

#鸟人类D
class BirdHuman(Bird,Human):
    #叫的方法
    def say(self):
        #鸟人叫 开始
        print('BirdHuman类 start')
        #调用鸟类的叫
        #调用人类的叫
        super().say()
        #鸟人叫结束
        print('BirdHuman类 end')


#实例化鸟人类
bh  = BirdHuman()
bh.say()


#查看MRO列表
print(BirdHuman.__dict__)
print(bh.__dict__)

#该成员属性继承来自object类
print(BirdHuman.__mro__)