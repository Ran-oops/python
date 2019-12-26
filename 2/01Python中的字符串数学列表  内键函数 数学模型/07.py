#数学函数


#abs 获取绝对值
num = -123.5

result = abs(num)

print(result)


#sum 计算一个序列的和（列表和元组集合）

lists = {1,2,234,6,21,57,156,7}

result = sum(lists)

print(result)

#max  & min  获取最大值/最小值（列表和元组集合）

lists = [12,56,1,67,23,87,2,8,0,457,99]

maxresult = max(lists)

print(maxresult)


minresult = min(lists)

print(minresult)


#pow 计算一个数值的N次方 用 ** 更快 很少

result = pow(3,4)

print(result)


#round() 四舍五入

num = 5.5

result = round(num)

#result = round(num,2)

print(result)


#range 产生一个连续的整型序列（生成器）

result = range(0,9)

print(result)

for i in result:
    print(i)




#只写结束值
result = range(20)

for i in result:
    print(i)


#带有间隔值的写法

result = range(0,101,5)


for i in result:

    print(i)

#max和min也接收多个数据的参数

result = max(12,56,1,67,23,87,2,8,0,457,99)

print(result)
