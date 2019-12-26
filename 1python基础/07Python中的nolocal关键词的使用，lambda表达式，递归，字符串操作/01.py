

#声明一个函数
def user():

    #局部变量
    #声明用户的名称
    name = '鲁大炮'
    #性别
    sex = '男'
    #年龄
    age = 28




    #内部函数
    
    #添加用户
    def adduser():
        print('添加用户的操作')

    #修改用户
    def moduser():
        print('修改用户操作')

    #删除用户操作
    def deluser():
        print('删除用户操作')

    #搜索用户
    def finduser():
        print('搜索用户操作')



    #使用return语句 返回信息
    def allinfo():
        #返回函数中需要返回的信息
        return adduser



    #为user函数返回信息
    return allinfo




#调用user函数
info = user()#返回值是allinfo      info = allinfo

#调用info函数相当于调用allinfo函数
auser = info()#返回值是adduser  auser = adduser

#调用内部函数auser 相当于调用adduser
auser()







'''
#希望在函数外部能够访问到这些局部变量和内部函数
info = user()#得到allinfo函数

#在次调用info函数 得到需要接受的局部变量和内部函数
auser = info()#得到allinfo函数的返回值  adduser 并且赋值给auser

#尝试调用添加用户操作
auser()
'''
    
