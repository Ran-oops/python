'''
#强制类型转换(显式数据类型转换)

intnum = 7758

floatnum = 5.21

#希望将浮点型转换为整型再运算
result = intnum + int(floatnum)

print(result)

'''


#int() 强制将其他数据转化为整型

#var = 3.998 #float类型
#var = 199 #int类型
#var = False #bool类型
#var = 10 + 2j #复数  无法转换
var = '+18'#字符串


#输出原有数据类型和值
print(type(var),var)

#转换为整型，并且输出类型和值
newvar = int(var)
print(type(newvar),newvar)
