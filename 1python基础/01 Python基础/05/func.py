#生成10行10列的星星

'''
#生成10行
hang = 0
while hang<10:
    #输出1行星星
    #1行10列
    lie = 0
    while lie<10:
        print('★',end = '')
        lie += 1

    #添加每行的换行符号
    print('\n',end ='')
    #行变量+1
    hang += 1
'''




#将特定功能制作成函数
def mystar():
    hang = 0
    while hang<4:
        #输出1行星星
        #1行10列
        lie = 0
        while lie<4:
            print('★',end = '')
            lie += 1

        #添加每行的换行符号
        print('\n',end ='')
        #行变量+1
        hang += 1

mystar()
mystar()
mystar()
