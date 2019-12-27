'''
#强制类型转换
intval = 250

floatval = 4.88

#强制类型转换
result = intval + int(floatval)

print(result)
'''

'''
#int()

#var = 350.56#浮点数
#var = '350'#纯整数字符串
#var = '350.54'#非纯整数字符串
#var  = 'only3cm'
#var = False
#var = 10

var = 5 + 2j

#输出原有数据类型和值
print(type(var))
print(var)

#类型转换
newvar = int(var)

#输出转换之后的类型和值
print(type(newvar))
print(newvar)
'''

'''
#float()
#var  = 3.1415926#浮点型
#var = 99 #整型
#var = False #布尔类型
#var = 5.3 + 2j#复数
#var  = '520.1314'
var = 'youhav520cm'


#输出原有类型和值
print(type(var))
print(var)

#类型转换
newvar = float(var)

#输出转换之后的类型和值
print(type(newvar))
print(newvar)
'''

'''
#bool()
#var = 0 #整型
#var = 0.0#浮点型
#var = 0 + 0j#复数
#var = ''#空字符串
#var = []#空列表
#var = ()#空元组
#var = {} #空字典
#var = set()#空集合


#输出原有类型
print(type(var))
print(var)

#类型转换
newvar = bool(var)

#输出新的类型值
print(type(newvar))
print(newvar)

'''


'''
#complex()
#var = 10#整型
#var = 3.1415#浮点数
#var = False
#var = '250.55'#整型和浮点字符串
var = '(5 + 6j)'

#输出原有类型和值
print(type(var))
print(var)

#类型转换
newvar = complex(var)

#输出转化之后的类型和值
print(type(newvar))
print(newvar)
'''


'''
#str()

#var = 10
#var = 250.45
#var = 2 + 1j
#var = True
#var = ['张三','李四','王老五']
var = ('张三','李四','王老五')

#输出原有类型和值
print(type(var))
print(var)
print(repr(var))
#类型转换操作
newvar = str(var)
#输出转化之后的类型和值
print(type(newvar))
print(newvar)
print(repr(newvar))
'''


'''
#list()

#var  = '少林功夫'
#var = (3,6,9,15)#元组
#var = {'韩琳琪','杨文峰','邵志诚'}#集合
#var = {'hlq':'韩琳琪','ywf':'杨文峰','szc':'邵志诚'}

#输出原有类型和值
print(type(var))
print(var)

#类型转换
newvar = list(var)

#输出转化之后的类型和值
print(type(newvar))
print(newvar)
'''

'''
#tuple()
var = '255.54'
var = {'hlq':'韩琳琪','ywf':'杨文峰','szc':'邵志诚'}
var = {'韩琳琪','杨文峰','邵志诚'}#集合

#输出原有类型和值
print(type(var))
print(var)

#类型转换
newvar = tuple(var)

#输出转化之后的类型和值
print(type(newvar))
print(newvar)
'''


#dict()
#var = ['黑猫警长','一只耳','请看下集']#以及列表无法转换

#var = [['cat','黑猫警长'],['mouse','一只耳'],['next','请看夏季']]
#var = [('cat','黑猫警长'),('mouse','一只耳'),('next','请看夏季')]
#var = (('cat','黑猫警长'),('mouse','一只耳'),('next','请看夏季'))
#var = (['cat','黑猫警长'],['mouse','一只耳'],['next','请看夏季'])

#输出原有类型和值
print(type(var))
print(var)

#类型转换
newvar = dict(var)

#输出转化之后的类型和值
print(type(newvar))
print(newvar)





'''
#set()
#var = {'hlq':'韩琳琪','ywf':'杨文峰','szc':'邵志诚'}
var = ['韩琳琪','杨文峰','邵志诚']

#输出原有类型和值
print(type(var))
print(var)

#类型转换
newvar = set(var)

#输出转化之后的类型和值
print(type(newvar))
print(newvar)
'''
