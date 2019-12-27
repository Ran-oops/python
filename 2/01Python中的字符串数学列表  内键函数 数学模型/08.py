#声明一个10进制的数字

num = 998

#转化为16进制

result = hex(num)

print(result)

#转化为8进制

result = oct(num)

print(result)

#转化为二进制

result = bin(num)

print(result)


#将内容以元字符串方式输出

str1 = '青蛙上了饭桌叫做\'炒田鸡\',癞蛤蟆摆在桌子上就是\'金蟾\'，着告诉\r我们一个问题，\n有理想是对么的重要'


print(str1)


result = repr(str1)

print(result)


#eval 将字符串当作python代码来执行 慎重使用

i = 99

str1 = 'i + 1 '

i = eval(str1)# i = i + 1 


print(i)


#python字符串

str1 = 'print("坐井观天")'

eval(str1)
