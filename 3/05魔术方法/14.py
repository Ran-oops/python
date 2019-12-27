#人类
class Human:
    #属性
    name = '文文'
    sex = 'nv'
    age = 18

    #方法
    def say(self):
        print('姚文涛，你真坏！')

    def cry(self):
        print('文涛，你的狗咬人了！～')

    #魔术方法
    def __format__(self,flag):

        #print(flag)
        #将标志拆分为三个部分：对其方式，总长度和填充符号
        result = flag.split('-')

        #对其
        dq = result[0]
        #长度
        cd = int(result[1])
        #填充符号
        tc = result[2]

        #判断对其方式
        if dq ==  'center':#剧中操作
            finalname = self.name.center(cd,tc)
        elif dq == 'left':#靠左对其
            finalname = self.name.ljust(cd,tc)
        elif dq == 'right':
            finalname = self.name.rjust(cd, tc)
        #必须有返回值，必须是字符串
        return finalname

#实例化对象
ww = Human()

#print(ww)


str1 = '姚文涛的小狗颜色真的很黄，{:left-10-@}很喜欢～'
result = str1.format(ww)
print(result)