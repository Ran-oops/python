#字典推导式

dict1 = {'duck':'鸭子','panda':'熊猫','snake':'蛇','dog':'狗','cat':'猫'}

#最简单的推导式

result = {key:value  for key,value in dict1.items()}

print(result)

#带有运算的推导式

result = {key:'●'+value+'●' for key,value in dict1.items()}

print(result)

#带有判断的推导式

result = {key:value for key,value in dict1.items() if key != 'snake'}

print(result)


#多循环的推导式

dict1 = {'长沙':'千里戈壁','开封':'新婚之夜','旅顺':'一路平安'}

dict2 = {'海口':'夸夸其谈','宁波':'风平浪静','青岛':'别太用力'}

result = {k1+k2:v1+v2 for k1,v1 in dict1.items() for k2,v2 in dict2.items()}

print(result)


#带有判断条件的多循环推导式

result = {k1+k2:v1+v2 for k1,v1 in dict1.items() for k2,v2 in dict2.items() if k1 == '开封' and k2 == '青岛'}

print(result)
