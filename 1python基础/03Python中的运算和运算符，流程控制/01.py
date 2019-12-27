#位运算

#按位与运算

var1 = 14#1110

var2 = 13#1101

result = var1 & var2

print(result)


#按位或运算

var1 = 29#11101

var2 = 14# 1110

result = var1 | var2

print(result)#11111


#按位非运算

var1 = 17#10001

result = ~var1

print(result)


#按位异或运算

var1 = 28
var2 = 20

result = var1 ^ var2

print(result)


#左移运算  相当于*2运算

var1 = 18#10010

result = var1 << 2

print(result)

#右移运算 相当于//2

var1 = 84

result = var1 >> 3

print(result)
