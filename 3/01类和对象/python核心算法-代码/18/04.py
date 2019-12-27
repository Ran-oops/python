#原始操作
'''
fp = open('2.txt','w')
fp.write('本草纲目')
fp.close()
'''


#读取文件
#with 语法  监控文件使用状态，在适当时候自动关闭

try:
    with open('1.txt','r') as fp:# 相当于 fp = open()
        print(fp.read())

except:
    print('文件打开出错！')
