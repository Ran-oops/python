#人类

class Human:
    #属性
    name = '美丽的姑娘'
    age = 18
    size = '36D'
    hair = 20

    #方法
    def eat(self):
        print('棒棒糖真好吃～')

    def drink(self):
        print('菌子汤中有添加鱼么？味道很鲜美')

    #魔术方法  触发时机： 使用repr（）操作对象的时候   作用：定义repr函数转换对象的结果   注意：绝大多数的str魔术方法和repr魔术方法相同即可
    def __repr__(self):
        pass

        #必须有返回值，必须是字符串
        return '露露是个会学习的姑娘122222！～'


    #保持repr魔术方法和str魔术方法一样
    __str__ = __repr__


#实例化对象
ll = Human()

result = repr(ll)
print(result)

result = str(ll)
print(result)