#break语句是循环中使用语句

#程序运行中一旦值为38 则结束循环
num = 0

while num<=100:

    #检测当前num的值是否是38
    if num == 38:
        #终止循环
        break
    
    print(num)
    num += 1
