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

    #魔术方法  触发时机：print（） 打印对象时候触发,或者使用str()操作对象时触发  作用 自定义打印对象信息
    def __str__(self):
        pass
        print('str被触发')

        #必须具有返回值，必须是字符串类型
        return '露露是个美丽的姑娘～'


#实例化对象
ll = Human()

print(ll)

# print(str(ll))