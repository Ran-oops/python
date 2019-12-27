#描述符

class Email:
    #属性
    #username = ''
    password = ''

    #方法
    pass

    def __init__(self):
        #用于和username进行映射的属性（自定义）
        self.myname = '小冰冰'

    #描述符操作
    @property#用于声明当前方法名称是一个成员属性，概属性的访问由当前方法控制（描述符的获取操作）
    def username(self):
        #print('执行了获取操作')
        result = self.myname[0]+'*'+self.myname[-1]
        return result

    @username.setter#(描述符的设置操作)
    def username(self,value):
        #print(value)
        self.myname = value

    @username.deleter#(描述符的删除操作)
    def username(self):
        #print('触发了删除操作')
        del self.myname


#实例化对象
email = Email()

#获取username
print(email.username)

#设置username
#email.username = '小超超'
#print(email.username)

#删除username
#del email.username
#print(email.username)       