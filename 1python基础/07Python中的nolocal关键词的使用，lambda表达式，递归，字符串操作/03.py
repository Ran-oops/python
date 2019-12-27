

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
        print(name,sex,age)
        print('添加用户的操作')

    #修改用户
    def moduser():
        print(name)
        print('修改用户操作')

    #删除用户操作
    def deluser():
        print(name)
        print('删除用户操作')

    #搜索用户
    def finduser():
        print(name)
        print('搜索用户操作')


    #直接返回局部变量(使用元组返回多个内部函数或者局部变量)
    return (adduser,moduser,deluser,finduser)


#接受user的返回值
result = user()
print(result)

#分别接受所有返回的内部函数
auser = result[0]
muser = result[1]
duser = result[2]
fuser = result[3]


#调用内部函数
auser()
muser()
duser()
fuser()


#__closure__
print(auser.__closure__)
