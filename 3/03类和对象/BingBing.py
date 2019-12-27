
class BingBing:

    #成员属性
    sex = 'woman'
    age = 21
    bf = 'unknow'
    height = 170


    #成员方法

    #带有self的方法称之为非绑定类的方法
    def say(self):#self的作用就是为了接收当前对象
        #print(self)
        print('老公，人家要买一个指甲油～')

    def eat(self):
        #输出当前对象的性别属性
        print(self.sex)
        print(self.age)
        #调用当前对象的say方法
        self.say()
        print('老板，来二两米饭')

    #不带有self的方法：绑定类的方法
    def drink():
        print('昨晚的菌子汤真好喝～')


#实例化对象
fb = BingBing()
print(fb,'实例化对象后的检测')

#调用对象的方法
fb.say()

#调用类的方法
BingBing.drink()


#友情提示：没人这么干！ 通过类方法带有self的方法
#BingBing.say(123)

#self的作用：使得对象使用某个方法时候可以调用对象的其他成员
fb.eat()

