
#10次猜数字小游戏
'''
#获取用户输入的操作
userinput = input()
print(userinput)
'''
'''
#商品价格
num = 98

#循环等待用户输入
i = 0
while i<10:
    #请输入您猜的价格
    user = int(input('请猜一猜当前的数字：'))

    #根据用户输入提示
    if user > num:
        print('你猜的数字太大了～')
    elif user < num:
        print('你猜的数字太小了～')
    else:
        print('恭喜您，答对了，可以把商品带回家！')
        #终止循环
        break

    #次数+1操作
    i += 1
#循环也有一个else分支
else:
    print('对不起，竞猜次数已经用完了！')

'''

#无限次的猜数字游戏(死循环)

#10次猜数字小游戏
'''
#获取用户输入的操作
userinput = input()
print(userinput)
'''
#商品价格
num = 98

#循环等待用户输入

while True:
    #请输入您猜的价格
    user = int(input('请猜一猜当前的数字：'))

    #根据用户输入提示
    if user > num:
        print('你猜的数字太大了～')
    elif user < num:
        print('你猜的数字太小了～')
    else:
        print('恭喜您，答对了，可以把商品带回家！')
        #终止循环
        break

#循环也有一个else分支
else:
    print('对不起，竞猜次数已经用完了！')
