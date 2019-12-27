

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


    #定义用户返回的函数
    def allinfo():
        return moduser

    
    #直接返回内部函数 （两部合成一部）
    return allinfo()

#调用user函数
muser = user()

#调用修改用户操作

muser()
