#人类

class Human:
    #属性
    name = '美丽的姑娘'
    age = 18
    size = '36D'
    hair = 20

    #方法
    def __init__(self):
        self.height = 180
        self.sex = 'nv'

    def eat(self):
        print('棒棒糖真好吃～')

    def drink(self):
        print('菌子汤中有添加鱼么？味道很鲜美')

    #魔术方法  触发时机：使用len（） 检测对象时触发
    def __len__(self):
        #获取对象的成员个数
        result = len(self.__dict__)

        #强制要求 返回值必须为整型
        return result

#实例化对象
ww = Human()

result = len(ww)
print(result)