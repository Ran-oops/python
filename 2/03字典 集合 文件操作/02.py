#遍历操作

dict1 = {'fish':'鱼','cow':'奶牛','monkey':'猴子','chick':'小鸡鸡'}

#for ..in 循环

for key in dict1:
    #遍历字典的键
    print(key)
    #遍历字典的值
    print(dict1[key])


#直接遍历键值对
#{'fish':'鱼','cow':'奶牛','monkey':'猴子','chick':'小鸡鸡'}
#[('fish','鱼'),('cow','奶牛')]...

#result = dict1.items()

#print(result)

for key,value in dict1.items():
    print(key,'----',value)
