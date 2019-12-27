class HuanHuan:
    #成员属性
    sex = '女'
    age = 21
    height = 170
    weight = '95kg'
    #私有化封装
    __heart = 'red'
    eye = 'black'


    #成员方法
    def say(self):
        #在对象内部访问成员
        print('我的心是{}颜色的'.format(self.__heart))
        self.__saniao()
        print('三百值鸭子在讲故事')

    def __saniao(self):
        print('徐徐徐徐！！～～')

    def run(self):
        print('别追我，给我机制糖浆')


#实例化对象
hh = HuanHuan()

#在对象外部访问成员heart(一旦成员进行了私有化封装，在对象外部无法进行任何操作)
#print(hh.heart)
#print(hh.__heart)

#在对象内部访问heart
#hh.say()

#私有化成员是python通过name mangling策略实现的，就是改名字
#print(HuanHuan.__dict__)

#打破规则，在类/对象外部访问呃私有成员（不推荐这么左）
#print(hh._HuanHuan__heart)


#在对象外部访问saniao方法
#hh.saniao()
#hh.__saniao()

#在对象内部访问saniao方法
#hh.say()

#打破规则，在类/对象外部访问呃私有成员（不推荐这么左）
hh._HuanHuan__saniao()