#人类
class Human:
    #属性
    sex = 'nan'
    age = 18

    #方法
    def say(self):
        print('洗完澡美美哒～')

    def cry(self):
        print('男朋友不要我啦～')

    #魔术方法  触发时机：把对象当作函数调用时触发  作用1：可以防止对象当作函数调用时出错！
    def __call__(self):
        print('call被触发')


#实例化对象
hh = Human()
#print(hh)

#把对象当函数使用
hh()


