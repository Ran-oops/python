
def user():

    #局部变量

    #定义添加用户操作
    def adduser():
        print('添加用户')
        
    #定义修改用户操作
    def moduser():
        print('修改用户操作')
        
    #定义查询用户操作
    def finduser():
        print('查询用户操作')
        
    #定义删除用户操作
    def deluser():
        print('删除用户操作')

    #使用闭包返回所有操作
    return (adduser,moduser,finduser,deluser)

#调用user函数
alluser = user()

zeng,gai,cha,shan = alluser

#print(alluser)

zeng()
gai()
