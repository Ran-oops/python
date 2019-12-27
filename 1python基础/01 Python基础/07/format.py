
#format字符格式化操作

#方法1  位置参数

#非关键字参数
str1 = '霍云瑞的身高是{},体重是{}'

result = str1.format('187cm','120KG')

print(result)


#多次利用参数
str1 = '霍云瑞的身高是{0},体重是{1}，{0}这个数值是他告诉我的'

result = str1.format('187cm','120KG')

print(result)


#关键字参数格式
str1 = '霍云瑞的身高是{height},体重是{weight}'

result = str1.format(weight = '120KG',height = '187cm')

print(result)


#方法2  通过下标

str1 = '霍云瑞的身高是{0[0]},体重是{0[1]}'

result = str1.format(('187cm','120KG'))

print(result)


str1 = '霍云瑞的身高是{0[h]},体重是{0[w]}'

result = str1.format({'h' : '187cm','w' : '120KG'})

print(result)


#方法3 格式限定符

#填充与对齐

str1 = '你拍一，我拍一，两个基佬打飞机！{:>10}'
str1 = '你拍一，我拍一，两个基佬打飞机！{:★>10}'
str1 = '你拍一，我拍一，两个基佬打飞机！{:★<10}'
str1 = '你拍一，我拍一，两个基佬打飞机！{:★^10}'

result = str1.format('我要飞得更高')

print(result)



#精度计算

str1 = '我能记住派的值，他的值大概是{:.4f}'

result = str1.format(3.141592653)

print(result)


#进制进制操作

str1 = '中午这顿饭，我吃了{}块钱'
str1 = '中午这顿饭，我吃了{:b}块钱'
str1 = '中午这顿饭，我吃了{:o}块钱'
str1 = '中午这顿饭，我吃了{:d}块钱'
str1 = '中午这顿饭，我吃了{:x}块钱'
result= str1.format(15)

print(result)


#金融字符 逗号分隔

str1 = '苹果这几天亏了{:,}钱'
result = str1.format(3000000000000)

print(result)




