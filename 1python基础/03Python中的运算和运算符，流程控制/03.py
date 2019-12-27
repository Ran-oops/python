#身份检测

var1 = '王元鹅'

print(id(var1))


var2 = '玩我鸟'

print(id(var2))


#操作

result = var1 is var2

print(result)


result = var1 is not var2

print(result)


#变量赋值

'''
#变量 = 变量 = 值  该方式创建的多个变量id标识一定相同

var1 = var2 = 2+3j

print(id(var1))
print(id(var2))

'''

#变量1 = 值
#变量2 = 值

var1 = {'1':'A','2':'B'}
var2 = {'1':'A','2':'B'}

print(id(var1))
print(id(var2))

