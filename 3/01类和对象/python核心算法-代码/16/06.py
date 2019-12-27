class Human:

    #属性(类)
    sex = 'man'
    age = 18
    height = 180

    #方法
    def __init__(self):
        self.name = '赛亚了'
        self.wife = '山崎行李'


    def say(self):
        print('邻家小妹没')

    def cry(self):
        print('5个大汉围在墙角')

    #魔术方法
    def __dir__(self):
        #print('dir备触发')
        #设置dir函数仅仅返回自定义成员
        #print(self.__dict__)
        #print(Human.__dict__)
        #获取对象中的成员名称
        objmembers = self.__dict__.keys()
        clsmembers = Human.__dict__.keys()


        lists = []
        for i in clsmembers:
            #不符合系统自带成员
            if (i.startswith('__') and i.endswith('__')) == False:
                lists.append(i)

        #将对象和类中成员合并
        lists += objmembers

        #必须有返回值，必须是容器类数据
        return lists


#实例化对象
sqxl = Human()

#dir（）函数  获取一个对象中所有可以访问的呃成员列表
result = dir(sqxl)
print(result)
print(result)
