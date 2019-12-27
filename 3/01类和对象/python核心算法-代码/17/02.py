#方法的分类

class Human:

    #类方法
    @classmethod
    def say(cls):
        print(cls)
        print('说话方法')


    #非绑定类的方法 对象方法
    def run(self):
        print('跑步方法')


    #静态方法   可以通过类也可以通过对象调用
    @staticmethod#可以省略
    def cry():
        print('哭泣方法')

    #绑定类的方法  只能通过类调用
    def eat():
        print('吃饭方法')

#访问三个方法
#对象方法
ll = Human()
ll.run()

#绑定类的方法
Human.eat()

#类方法
Human.say()

#静态方法
Human.cry()
ll.cry()