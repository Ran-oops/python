#人类

class Human:
    #属性
    name = '美丽的姑娘'
    age = 18
    size = '36D'
    hair = 20
    sex = 'woman'

    #方法
    def eat(self):
        print('棒棒糖真好吃～')

    def drink(self):
        print('菌子汤中有添加鱼么？味道很鲜美')

    #魔术方法  触发时机：使用bool（）操作对象的时候触发
    def __bool__(self):
        print('bool方法呗触发')
        #制作性别检测功能
        if self.sex == 'man':
            #必须具有返回值，必须是布尔类型
            return True
        else:
            return False


#实例化对象
ll = Human()
print(ll)


#对象转化为布尔值(用于检测用户性别)
result= bool(ll)
print(result)
