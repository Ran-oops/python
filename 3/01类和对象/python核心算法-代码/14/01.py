#继承
class Father:
    #成员属性
    __sex ='man'
    age = 18
    wife = '围裙妈妈'


    #成员方法
    def say():
        print('孩子，你妈呢')

    def xuxu(self):
        print('哗哗哗哗～～')

class Son(Father):
    pass


#检查儿子类
print(Son.__dict__)

#访问儿子类的性别
# print(Son.sex)
print(Son.age)
Son.say()