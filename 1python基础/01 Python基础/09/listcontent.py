#简单的列表推导式
list1 = ['亚古兽','暴龙兽','机械暴龙兽','丧尸暴龙兽','战斗暴龙兽']

result = ['◎'+i+'◎' for i in list1]

print(result)

#带有判断条件的列表推导式

list1 = [1,32,4,5,2,67,1,457,9,2,568,21,45,1,34]

result = [i for i in list1 if i % 2 == 0]

print(result)

#多个列表的推导式

list1 = ['黄土','两条龙','小灯泡','大乔','小乔']
list2 = ['高坡','王二龙','杨小亮','乔宽宽','乔琦']

result = [x + '=>'+ y for x in list1 for y in list2]

print(result)

#多个列表推导式 带有判断条件1

num1 = [2,4,6,8,9]
num2 = [4,16,36,64,81]
#s使用表达式中的值作为判断条件
result = [x + y for x in num1 for y in num2 if y == x*x ]
print(result)


#多个列表推导式 带有判断条件2
list1 = ['黄土','两条龙','小灯泡','大乔','小乔']
list2 = ['高坡','王二龙','杨小亮','乔宽宽','乔琦']


result = [x + '=>'+y for x in list1 for y in list2 if list1.index(x) == list2.index(y)]

print(result)
