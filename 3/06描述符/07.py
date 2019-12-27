#声明类
#自定义类来继承系统的整形类
class myint(int):

    #魔术方法  触发时机：当前对象+另外一个数值的时候触发
    def __add__(self,other):
        #print('add被触发')

        return int(self) - int(other)


    #魔术方法  触发时机：当前对象-另外一个数值的时候触发
    def __sub__(self,other):
        #print('sub备触发')

        return int(self) + int(other)


    #魔术方法 触发时机：当前对象*另外一个数值的时候触发
    def __mul__(self,other):
        #print('mul备触发')

        return int(self) / int(other)

    #魔术方法  触发时机：当前对象/另外一个数值的时候触发
    def __truediv__(self,other):
        #print('__truediv__ 备触发')

        return int(self) * int(other)





#实例化对象
one = myint(10)#相当于int（10）

#加法操作
#result = one + 20
#print(result)


#减法操作
#result = one - 2
#print(result)


#乘法操作
#result = one * 5
#print(result)

#除法操作
#result = one / 4
#print(result)