
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


    #通过return语句和容器数据将局部变量和内部函数返回
    return (boy,girl,chedan,smoking)


#调用内部函数和局部变量
# print(boy)
# print(girl)
# chedan()
#smoking()


#调用函数获取所有的返回值

result = py02()
# print(result)

#高级写法
# nan,nv,cd,chou = result
print(result)
#初级写法
# nan = result[0]
#nv  = result[1]
#cd  = result[2]
#chou = result[3]

# print(nan)
# print(nv)
# print(cd)
# print(chou)

#调用内部函数
# chou()



