#continue  继续


#遍历0-100的所有数据  有4的就不要

num = 0

while num <=100:
    #判断数字中是否带有4
    if num % 10 == 4 or  (num >=40 and num <50):
        num += 1
        continue#continue执行之后当前循环的后续代码都不会执行
    
    print(num)
    num += 1
