#装饰器   为成员方法扩展功能 这就是装饰器

'''
#1.普通的函数
def laxi():
    print('噗～  噌噌噌～  哗啦啦啦～')

#调用函数
laxi()
laxi()
'''

'''
#2.为函数扩展功能（不是装饰器）
def zhuangshi(func):
    #增加功能
    print('烧香拜佛，祈求一切顺利')
    #使用原有功能
    func()
    #增加功能
    print('烧香还愿，感谢佛祖保佑～～')




def laxi():
    print('噗～  噌噌噌～  哗啦啦啦～')

#进行功能扩展并且再次赋值给原函数（调用laxi 因为zhuangshi函数没有返回值所以为None）
laxi = zhuangshi(laxi)


#把函数作为参数传入另外一个函数中


laxi()
laxi()
'''
'''
#3.为函数扩展功能，可以使用
def zhuangshi(func):

    #声明一个内部函数
    def inner():
        # 增加功能
        print('烧香拜佛，祈求一切顺利')
        # 使用原有功能
        func()
        # 增加功能
        print('烧香还愿，感谢佛祖保佑～～')

    #返回内部函数inner
    return inner




def laxi():
    print('噗～  噌噌噌～  哗啦啦啦～')

#进行功能扩展并且再次赋值给原函数（调用laxi 因为zhuangshi函数没有返回值所以为None）
laxi = zhuangshi(laxi)


#把函数作为参数传入另外一个函数中

laxi()
laxi()
'''

'''
#4.真正的装饰器语法
def zhuangshi(func):

    #声明一个内部函数
    def inner():
        # 增加功能
        print('烧香拜佛，祈求一切顺利')
        # 使用原有功能
        func()
        # 增加功能
        print('烧香还愿，感谢佛祖保佑～～')

    #返回内部函数inner
    return inner



@zhuangshi  #等价于laxi = zhuangshi(laxi)
def laxi():
    print('噗～  噌噌噌～  哗啦啦啦～')




#把函数作为参数传入另外一个函数中

laxi()
laxi()
'''
'''
#5.带有参数和返回值的函数
def zhuangshi(func):#func用于接收呗装饰的函数

    #内部对接收的函数功能func进行扩展
    def inner(w,n):#inner是未来装饰之后的laxi函数
        # 增加功能
        print('烧香拜佛，祈求一切顺利')
        # 使用原有功能（调用laxi函数）
        result = func(w,n)
        # 增加功能
        print('烧香还愿，感谢佛祖保佑～～')

        #因为laxi函数具有返回值，当前inner作为扩展之后的laxi函数也必须具有返回值
        return result

    #返回扩展之后的函数
    return inner

@zhuangshi

def laxi(who,num):
    print(who,'拉了',num,'斤便便～')
    #添加返回值
    return '屎'

result1 = laxi('吴小伟',200)
print(result1)

result2 = laxi('米冬涛',0.1)
print(result2)
'''

'''
#6.带有收集参数的函数 装饰器
#定义装饰器函数
def zhuangshi(func):
    #新建内部函数用于扩展函数功能
    def inner(*w,**n):
        #增加功能
        print('敲锣打鼓，通告天下')
        #调用原来的拉稀函数
        func(*w,**n)
        #增加功能
        print('放鞭炮，庆祝成功，顺便肥沃了土地！')


    #返回扩展之后的函数
    return inner

@zhuangshi
def laxi(*whos,**nums):
    print('一堆人参与拉屎！')
    print('参与集体拉屎的人有：',whos)
    print('分别拉了多少斤',nums)


#调用拉稀函数
laxi('欢欢','冰冰','露露','文文',hh = 1,bb = 2 ,ll = 30, ww = 4)
'''
'''
#7.带有参数的装饰器

#装饰器函数
def zhuangshiqi(type):#type 接收装饰器的参数
    def _zhuangshiqi(func):#func 接收需要装饰的函数
        #扩展函数功能  扩展拉稀
        def innerla():
            #增加功能1
            print('脱下裤子，准备拉屎')
            #调用基本函数拉稀
            func()
            #增加功能2
            print('擦屁股，提裤子走人')


        #扩展函数功能  扩展吃屎
        def innerchi():
            #增加功能1
            print('餐前要洗手～')
            #调用基本功能 吃
            func()
            #增加功能2
            print('吃完之后，擦嘴，剃牙！')

        #根据装饰器的参数返回不同的装饰之后的函数
        if type == 'la':
            return innerla
        elif type == 'chi':
            return innerchi

    #返回装饰器
    return _zhuangshiqi


#基本函数1
@zhuangshiqi('la')
def laxi():
    print('噌噌～～ 噗次～～')

#基本函数2
@zhuangshiqi('chi')
def chishi():
    print('这坨便便太稀了，需要用勺子蒯这吃～')


laxi()

chishi()
'''

'''
#8.使用类作装饰器的参数
#祈福的类
class Wish:

    #方法1
    def before():
        print('烧香拜佛，祈求一切顺利')

    #方法2
    def after():
        print('烧香还愿，感谢佛祖保佑！～')


#当前这一层装饰器用于接收参数
def zhuangshiqi(cls):
    #这一层装饰器用于接收基本函数
    def _zhuangshiqi(func):
        #扩展函数功能
        def #inner():
            #增加功能1
            cls.before()
            #调用基本功能
            func()
            #增加功能2
            cls.after()

        #返回装饰之后的函数
        return inner


    return _zhuangshiqi

#基本函数
@zhuangshiqi(Wish)
def laxi():
    print('噌噌～～ 噗次～～')

laxi()

'''
'''
#9.使用类作为装饰器使用
class Zhuangshiqi:

    #魔术方法   接收装饰器的参数（不一定用的上，取决于装饰器是否传参）
    def __init__(self,arg):
        #print(arg)
        #将装饰器的参数入存入当前对象
        self.arg = arg


    #一个用于接收基本函数zhuangshiqi
    def __call__(self,func):
        #将传入的基本函数func 存入对象
        self.func = func

        return self.inner

    #一个用于扩展函数  inner
    def inner(self):
        # 增加功能1
        print('烧香拜佛，祈求一切顺利')
        # 调用基本功能
        self.func()
        # 增加功能2
        print('烧香还愿～')

@Zhuangshiqi(5) #此处可以传入参数，需要init接收，但是传不传取决于程序需求
def laxi():
    print('噌噌～～ 噗次～～')

laxi()
'''

'''
#10.为类添加装饰器

objdict = {}

#装饰器函数
def zhuangshiqi(cls):

    #装饰器的内部函数  (inner函数的结果就是 类调用的结果)
    def inner():
        #检测是否创建过对象
        if 'only' in objdict:#对象已经创建过
            return objdict['only']
        else:
            #创建对象，存入字典
            obj = cls()
            objdict['only'] = obj
            return objdict['only']

    return inner

#冰冰类
@zhuangshiqi
class BingBing:
    sex = 'nv'
    age = 18
    bf = '不认识，学java的'

    def say(self):
        print('老公，你轻点，揉的太疼了！')


#实例化冰冰
one = BingBing()
print(one)

two = BingBing()
print(two)

three = BingBing()
print(three)
'''
'''

#11.多装饰器的使用
#装饰器函数1
def zsq1(func):

    #创建内部函数inner
    def inner():
        print('脱裤子')
        func()
        print('提裤子')

    return inner

#装饰器2
def zsq2(func):

    #创建内部函数
    def inner():
        print('烧香拜佛，祈求一切顺利')
        func()
        print('烧香还愿！～')

    return inner


@zsq2
@zsq1
def laxi():
    print('吃啥拉啥，那就只能吃屎了～')

#调用函数
laxi()
'''