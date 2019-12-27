#描述符2

class Email:
    #属性
    username = None
    password = None

    #用于作为描述符的映射变量的成员属性
    def __init__(self):
        self.myname = '铁蛋'#为了和username属性关联

    #方法
    pass

    #描述符的三个操作方法
    #获取的描述符方法
    def getusername(self):
        #print('执行了描述符的获取方法')
        #返回的名字中间+星号
        result = self.myname[0]+'*'+self.myname[-1]
        #为描述符的返回结果
        return result

    #设置的描述符方法
    def setusername(self,value):
        #可以在设置时做其他限制
        self.myname = value

    #删除的描述符方法
    def delusername(self):
        #print('执行了描述符的删除操作')
        del self.myname

    #设置描述符方法的操作(完成了username属性和描述符的关联)
    username = property(getusername,setusername,delusername)


#实例化对象
email = Email()


#访问username
#print(email.username)


#设置username
#email.username = '小欢欢'
#print(email.username)

#删除username
del email.username
print(email.username)