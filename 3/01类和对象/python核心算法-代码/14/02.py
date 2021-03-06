'''
定义方法的时候加了self，那么在调用这个类中的方法时就必需要实例化一个对象，即：类（对象）.方法（参数）
定义方法的时候没有加self，那么调用这个类的方法时就可以直接调用方法，即：类.方法（参数）
'''



#受保护的封装操作  操作Die类
class Die:
    #成员属性
    familyName = '吴'
    #受保护的操作  在前面加一个下划线
    _money = '100'
    sex = 'man'
    agee = 18

    #成员方法
    def song():
        #检测类/对象内部是否可以访问受保护成员
        print(Die._money)
        Die._run()
        print('大风车吱呀只有有的转，TMD，TMD真好看～')

    def _run():
        print('救命啊～ 老婆别打我～')


#继承操作 测试子类访问情况
class Erzi(Die):

    #测试在子类中访问父类的受保护成员
    def test():
        print(Erzi._money)
        Erzi._run()


#类外部访问成员   可以访问的，理论上不应该可以访问到
# print(Die.money)
# print(Die._money)#理论上不应该可以访问到，但是可以！

#类内部访问成员   可以访问
# Die.song()

#子类内部访问父类受保护成员
Erzi.test()



#1.类中和对象中  概念是一致的，因为类的结构就是未来对象的结构
#2.子类也是类，子类中和子类对象中的概念是一致的
#3.
    #公开的   (类中/类外/子类中)
    #受保护   (类中/子类中)
    #私有的   (类中)