''' 全局变量检测
#函数外部
boss = '张晓光'#全局变量

#使用全局变量boss(函数外/全局)#使用全局变量boss(函数外/全局)
print(boss)


def py01():


    #使用全局变量boss(函数内/局部)
    print(boss)

#调用函数
py01()

'''


''''''
#局部变量检测
def py01():
    
    #函数内部
    stu = '杨小亮'#局部变量
    
    #局部中使用局部变量
    #print(stu)

#调用函数
py01()

#使用局部变量
print(stu)




'''
#修改全局变量

#函数外部
boss = '张晓光'#全局变量

def py01():

    #将变量设置为全局变量
    global boss

    #尝试修改全局变量
    boss = '李超'

#调用函数
py01()

#调用修改之后的boss变量
print(boss)
'''


