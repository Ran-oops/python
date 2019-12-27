#实现闭包操作3  不常见的使用方法
#全局环境

#用于获取所有局部变量
allinner = None


#函数局部环境
def py02():

    #全局化声明allinner
    global allinner
    
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

    #将getall函数赋值给allinner
    allinner = getall


#调用函数py02
py02()

#直接使用allinner变量
print(allinner)

#调用函数（getall）获取getall的返回值
allvar = allinner()

print(allvar)

   
