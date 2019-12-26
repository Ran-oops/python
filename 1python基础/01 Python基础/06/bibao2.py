
#实现闭包操作1

#全局环境


#函数局部环境
def py02():
    #局部变量
    boy = '霍云瑞'
    girl = '李雪'
    yao = '晶晶'

    #内部函数
    def chedan():
        print('曹睿和曹俊良正在互相扯淡！')

    def smoking():
        print(yao,'正在吸食香烟～')


    
    
    #获取所有需要进行闭包的函数和变量，通过return返回

    def getall():
        #获取所有需要返回的数据
        return (boy,girl,chedan,smoking)


    #返回getall函数
    return getall


#调用函数

result = py02()
print(result)

#在此调用getall函数(已经变成result)

allvar = result()
print(allvar)

#使用变量获取元组中每个值
nan,nv,cd,chou = allvar

print(nan)
print(nv)
cd()
chou()
