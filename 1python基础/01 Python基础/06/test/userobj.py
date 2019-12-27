class User:

    #定义添加用户操作
    def adduser(self):
        print('添加用户')
        
    #定义修改用户操作
    def moduser(self):
        print('修改用户操作')
        
    #定义查询用户操作
    def finduser(self):
        print('查询用户操作')
        
    #定义删除用户操作
    def deluser(self):
        print('删除用户操作')


#实例化对象
user = User()

user.adduser()
user.deluser()
