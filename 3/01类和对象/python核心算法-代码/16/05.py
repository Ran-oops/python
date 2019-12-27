class Human:

    #属性
    def __init__(self):
        self.name = '浪浪'
        self.age = 18
        self.sex = 'man'

    #方法
    pass

    #魔术方法  触发实际：访问呃成员属性时候触发（无论属性是否存在）
    def __getattribute__(self, attrname):
        print('__getattribute__ 被触发')
        #print(attrname)

        if attrname == 'sex':
            return 'woman'
        elif attrname == 'age':
            return 38
        else:
            return '就不告诉你'

    #注意：getattribute和getattr魔术方法同时存在，只可能触发getattribute
    def __getattr__(self,attrname):
        print('__getattr__呗触发')



#实例化对象
ll = Human()
#print(ll.__dict__)

#访问已存在的属性
#print(ll.sex)
#print(ll.age)
#print(ll.name)
print(ll.wife)