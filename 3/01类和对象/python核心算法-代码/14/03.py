#被别人继承的类 ->父类/超类/基类
class LiuBei:
    #成员属性（类的财产）

    familyName = '刘'#姓
    firstName = '备'#名
    money = '蜀国'
    sex = '男'
    __wife = '孙尚香，靡夫人'
    age = 48

    #成员方法（类的财产）
    def say():
        print('个位爱卿，有何良策')

    def cry():
        print('你这个小畜生，竟然险损我一员大將')

    def makeshoes(self):
        print('我的草鞋，时尚时尚最时尚～')

    #非绑定类的方法 对象访问
    def fire(self):
        print(self.__wife)
        print('打死你个龟孙！')



#继承别人的类->子类/派生类
class LiuChan(LiuBei):#实现类的继承操作

    #子类独有的成员
    weight = 180
    height = 165

    #子类中的属性和父类重名
    firstName = '禅'


    def xiangle():
        print('我爸爸是刘备！')

    #子类中的方法和父类重名
    def cry():
        print('5555!~~~')

    def say():
        #1.父类的say的内容在此处操作（调用父类的say方法）
        LiuBei.say()
        #2.子类say方法香说的话
        print('爸爸，我妈去哪里了')
        
    #子类重载父类的fire方法  必须用对象访问
    def fire(self):
        #1.父类中的fire方法执行一边
        #LiuBei.fire(self)#不推荐
        super().fire()#在此处的位置相当于调用当前类的父类对象中的fire方法
        #2.子类的操作
        print('打死你个鳖肚子！')



# 查看LiuChan类（子类）是否具有LiuBei类（父类）的成员
# print(LiuBei.__dict__)
# print(LiuChan.__dict__)
#
# print(LiuChan.age)
# print(LiuChan.sex)
# LiuChan.say()
# LiuChan.cry()
#
#
#
# 访问子类独有的成员
# print(LiuChan.height)
# print(LiuChan.weight)
# LiuChan.xiangle()
#
#
#
# 访问子类和父类同名的方法/属性    使用子类成员  如果子类的方法和父类重名，这种操作称之为方法的重载
# LiuChan.cry()#使用子类的方法
# print(LiuChan.firstName)
#
#
# 方法重载中，调用父类的操作
# LiuChan.say()
#
# 实例化子类对象
lc = LiuChan()
lc.fire()
