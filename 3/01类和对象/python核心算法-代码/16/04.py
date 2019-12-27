#与属性操作相关的魔术方法

class Human:
    #属性

    age = 18
    name = '伟哥'

    def __init__(self):
        self.sex = 'man'

    #方法
    #魔术方法 触发实际：访问不存在的属性时候触发
    def __getattr__(self,attrname):
        #print('getattr触发')
        if attrname == 'length':
            return '180cm'
        elif attrname == 'height':
            return '120cm'
        else:
            return '就不告诉你！'

    #魔术方法  触发实际：对成员属性进行设置值的时候触发
    def __setattr__(self,attrname,value):
        #print('setattr触发')
        if attrname == 'sex':
            object.__setattr__(self, attrname, value)
        elif attrname == 'age':
            #不可以使用对象.成员名称 进行设置，会触发递归操作，必须借助object来实现
            object.__setattr__(self,attrname,value)
        else:
            pass

    #魔术方法
    def __delattr__(self,attrname):
        #print('delattr呗除法',attrname)
        if attrname == 'sex':
            object.__delattr__(self,attrname)
        elif attrname == 'age':
            pass

    def run(self):
        print('帝国主义夹着尾巴，住着拐杖，端着反喷逃跑了！')



#实例化对象
weige = Human()

#访问不存在的属性
#print(weige.length)
#print(weige.height)
#print(weige.weight)

#设置成员属性
#weige.age = 28
#print(weige.age)

#weige.name = '小伟个'
#print(weige.name)


#删除成员属性
del weige.sex
print(weige.sex)