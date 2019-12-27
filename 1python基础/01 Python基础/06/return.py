'''
#声明一个变量
var = 100

#获取id值
result = id(var)
print(result)

#获取print的值
result = print(var)
print(result)
'''

'''
#执行过程函数
def papapa1():
    print('一阵不可描述之后～')
    print('一阵不可描述之后～')
    print('一阵不可描述之后～')


result = papapa1()
print(result)


#具有返回值的函数
def papapa2(): 
    print('一阵不可描述之后～')
    print('一阵不可描述之后～')
    print('一阵不可描述之后～')

    #为当前函数返回一个值
    return '孩子一个'

result = papapa2()
print(result)

'''

'''
#具有返回值的函数
#传入一个字符串，将字符两边添加一个★，返回修改之后的哦字符串

def strstar(arg):

    #进行字符串修改操作
    result = '★'+arg+'★'
    #将修改之后的字符串作为函数的返回值返回
    return result


newstr = strstar('高坡')
print(newstr)
print(newstr)
print(newstr)
print(newstr)
#将数据存储到文件中
fp = open('1.txt','w')
fp.write(newstr)
fp.close()
'''

'''
#计算N个数的阶乘并且返回结果
def jiecheng(*args):
    #初始计数变量
    total = 1

    
    #遍历参数元组 计算乘积
    num = 0
    while num<len(args):
        total *= args[num]
        num += 1

    #打印这个结果
    #print(total)
    #返回计算结果
    return total

    #尝试return之后执行代码
    print('擦屁股')

result = jiecheng(2,3,5,7)
print(result)
print(result)
print(result)
'''

'''
#检测男女差距函数
def checksex(sex):
    #根据不同的性别返回不同的特征
    if sex == '男':
        return '70岁'
    elif sex == '女':
        return '77岁'


result = checksex('男')
print(result)  #相当于print(checksex('男'))

result = checksex('女')
print(result)
'''

#一个函数返回多个值
def moreval():
    #要返回3个人名  乔宽，乔窄，乔塌了
    return '乔宽','乔窄','乔塌了'


result = moreval()
print(result)
