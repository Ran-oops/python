'''
人类：
    特征部分
    年龄  26
    性别  男
    肤色  黄色
    眼睛  1.2
    身高  180cm
    长度  180mm
    。。。。。


    功能部分
    说话
    liao妹
    跑
    讲课
    抽人
    开车
    。。。。


'''
class Human:

    #特征部分
    age = 26
    sex = 'man'
    color = 'yellow'
    eye = 1.2
    height = '180cm'
    length = '180mm'
    time = '180mins'



    #功能部分
    def say():
        print('一夜70次郎')

    def liaomei():
        print('妹子，这个砖头是你掉的么？')

    def run():
        print('哎呀，吴小伟耍流氓啦～ 快跑啊～')

    def hit(self):#通过对象访问，一定会把对象作为实参传入方法中
        print(self)
        print('吴小伟拿着蜡烛滴女人啦～')

    def drive(self):#通过对象访问，一定会把对象作为实参传入方法中
        print(self)
        print('吴小伟在骑自行车啊～')

# #实例化对象
wxw = Human()
#
# #检测对象信息
# print(wxw)
#
# print(type(wxw))
#
# print(id(wxw))
#
#
# #检测类信息（类名也是变量）
# print(Human)
#
# print(type(Human))





#检测类中的成员
# print(Human.__dict__)

#检测对象中的成员
# print(wxw.__dict__)


#类成员的操作

#访问类中的成员属性
# print(Human.length)
# #调用类中成员方法
# Human.run()
# #访问类中成员方法
# print(Human.run)


#添加成员属性操作
# Human.weight = '90kg'
# #添加成员方法操作
# #Human.cry = lambda :print('妈妈救命啊～')
#
# def mycry():
#     print('5555~~')
#
# Human.cry = mycry
#
#
# #修改类中成员属性
# Human.color = 'black'
# #修改类中成员方法
# #Human.run = lambda :print('小屋咬人啦，快点跑啊！')
# def myrun():
#     print('人配衣裳马配鞍,狗配铃铛跑得欢')
#
# Human.run = myrun
#
#
# #删除类中成员属性
# del Human.color
# del Human.time
#
# #删除类中成员方法
# del Human.hit
# del Human.liaomei
#
#
#
#
# print(Human.__dict__)
#
# Human.run()
#
#
#
# #对象成员的操作
#
# # print(wxw.__dict__)


#访问对象成员属性
# print(wxw.sex)
# print(wxw.age)
# #访问对象的成员方法
# wxw.drive()
# wxw.hit()


#对象成员属性修改
wxw.sex = 'woman'#看起来是修改对象成员，由于对象中本来就没有成员门本质上是添加成员
print(wxw.sex)
#对象成员方法的修改
wxw.hit = lambda : print('大飞机！')#看起来是修改对象成员，由于对象中本来就没有成员门本质上是添加成员
print(wxw.__dict__)

'''
#添加对象成员属性
wxw.jj = '0.05m'
#添加对象成员方法
wxw.penshui = lambda : print('伟哥会喷水，也会喷火！')


#删除对象成员属性
del wxw.jj
#删除对象成员方法
del wxw.penshui


print(wxw.__dict__)
'''