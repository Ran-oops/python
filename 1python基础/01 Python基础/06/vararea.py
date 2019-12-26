

#声明一个函数

#函数外部
boss = '张晓光'#全局变量

#使用全局变量boss(函数外/全局)
#print(boss)
def py01():

    #将全局变量完全引入函数内部
    # global boss
    
    #函数内部
    stu = '杨小亮'#局部变量

    #使用全局变量boss(函数内/局部)
    # print(boss)

    #局部中使用局部变量
    #print(stu)

    #尝试修改全局变量
    boss = '李超'
    # print(boss)


#调用函数
py01()


#使用局部变量
print(stu)


#调用修改之后的boss变量
print(boss)
