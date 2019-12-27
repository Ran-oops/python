#描述符  对成员属性的操作进行控制

#描述符的类
class Description:#（道士）

    #为当前描述符对象添加一个成员属性 接收管理的属性username
    def __init__(self):
        self.myname = '王饼环'#（道士手中用来关联露露的稻草人）

    #成员属性的访问操作
    def __get__(self,obj,cls):
        #print(obj,cls)
        #对成员属性进行操作（为用户名隐藏中间文字）
        result = self.myname[0]+'*'+self.myname[2]
        return result

    #成员属性的设置操作
    def __set__(self,obj,value):
        #设置操作
        self.myname = value

    #成员属性的删除操作
    def __delete__(self,obj):

        #删除了描述符对象中用于接收Email类成员属性username的成员属性myname，就相当于删除了username
        del self.myname



#邮箱类
class Email:
    #属性
    #实例化一个描述负对象来管理某个成员属性（交接工作）
    username = Description() #用户名（露露）
    password = None #密码

    #方法
    pass


#实例化邮箱对象访问其中的username成员属性
email =  Email()

#获取成员属性的操作
# print(email.username)

#设置成员属性的操作
email.username = '刘老根'
print(email.username)


#删除成员属性的操作
del email.username
print(email.username)