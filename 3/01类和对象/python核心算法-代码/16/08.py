#声明类

class myint(int):

    #魔术方法   触发实际：数据 + 当前对象的时候触发
    def __radd__(self,other):
        #print(self,other)

        return int(other) - int(self)



#实例化对象
one = myint(50)

#加法操作
result = 30 + one
print(result)
