#string模块  主要提供字符归类查询

#导入模块
import string

#输出所有空白字符  whitespace
str1 = string.whitespace

#将字符串转化成元字符
result = repr(str1)

print(result)


#输出所有ascii码的小写字母 ascii_lowercase

str1 = string.ascii_lowercase

print(str1)


#输出所有ascii码的大写字母 ascii_uppercase

str1 = string.ascii_uppercase

print(str1)

#获取所有ascii码的字母ascii_letters

str1 = string.ascii_letters

print(str1)

#所有十进制数字字符 digits

str1 = string.digits

print(str1)


#所有十六进制字符 hexdigits

str1 = string.hexdigits

print(str1)


#所有八进制数字 octdigits

str1 = string.octdigits
print(str1)

#所有标点符号

str1 = string.punctuation

print(str1)


#所有可以打印的字符
str1 = string.printable

print(str1)



'''
常用ascii码的范围

数字  0-9  ascii  48-57

大写字母 A-Z  ascii  65-90

小写字母 a-z  ascii  97-122

'''


