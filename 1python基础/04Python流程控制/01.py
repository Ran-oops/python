#float浮点类型转换

var = 128#整型
var = False #布尔值
var = '-3'#字符串



#输出原有数据类型和值
print(type(var),var)

#类型转换操作
newvar = float(var)

#输出转换之后的类型和值
print(type(newvar),newvar)


#complex 复数转换

var = 256 #整型
var = 250.41 #浮点数
var  = False #布尔型
var = '12.5'#字符串

#输出原有类型和值
print(type(var),var)

#类型转换操作
newvar = complex(var)

#输出转换之后的类型和值
print(type(newvar),newvar)


#bool类型转换

var = 0#整型
var = 0.0#浮点
var = False #布尔值
var = 0+0j#复数

var = ''#字符串

var = [] #列表
var = () #元组
var = {} #字典
var = set()#集合

#输出原有类型和值
print(type(var),var)

#类型转换操作
newvar = bool(var)

#输出转换之后的类型和值
print(type(newvar),newvar)


