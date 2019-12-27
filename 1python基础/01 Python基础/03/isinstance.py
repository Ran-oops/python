var1 = 100.5

#检测var1是否是整型

#result = isinstance(var1,int)

#检测var1是否是浮点型

#result = isinstance(var1,float)

#检测var1是否是字符串

#result = isinstance(var1,str)

#禁止检测任意数据是否是object做的
result = isinstance(var1,object)

print(result)
