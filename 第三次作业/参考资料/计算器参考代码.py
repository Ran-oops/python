
import tkinter
import math



class Demo:
    bj = False # 标志符 判断按键是否按下
    lists = [] #  定义空列表
    bj1 = False #标志符
    lists1 = [] # 定义空列表,来接收键盘输出的元素


    def __init__(self):





        # 定义空列表
        self.root = tkinter.Tk()
        self.root.minsize(368, 473)
        self.root.title('智能小计算器')
        self.showlabel()
        self.root.mainloop()

    # 定义数字被按下的函数
    def num(self,num):

        print(num)
        if self.bj == True: #标志符,判断数字是否被输入
            self.v.set('0')
            self.bj = False
        # 判断面版里的值是否为初始值0
        if self.v.get() == '0':

            self.v.set(num)
            self.v1.set(num)
            if self.v.get() =='.' : #  实现小数的输入
                self.v.set('0' + num)
                self.v1.set('0' +num)

        else: #面板里的初始值不为0
            if self.v.get().count('.') ==0: #如果小数点的个数不为0
                self.v.set(self.v.get() + num)
                self.v1.set(self.v1.get()+num)
            elif num != '.': #判断第二个输入的数值不为小数点

                self.v.set(self.v.get() + num)
                self.v1.set(self.v1.get()+num)




    # 定义一个运算被按下的函数

    def ys(self,ys):

        self.lists.append(self.v.get())
        self.lists.append(ys)#见运算符和数字拼接在一起
        print(self.lists)
        self.v1.set(self.lists)


        self.bj = True # 标志符  判断运算 + - * /等是否被输入

    # 删除操作(删除输入数据的最后一位)
    def delete(self):
        if self.v.get() == '' or self.v.get() == '0':
            self.v.set('0')
            return
        else:
            num = len(self.v.get())
            if num > 1: #如果字符窜长度为大于一,删除操作会删除最后以为数字
                strnum = self.v.get()
                strnum = strnum[0:num - 1]
                self.v.set(strnum)
                self.v1.set(strnum)

            else:
                self.v.set('0')
                self.v1.set('0')

    #撤消用户上一步输入的数据 操作 (删除因用户失误输入的数据)
    def ce(self):
        if self.v.get() != '' or self.v.get() != '0':#判断 是否在显示面板输出了数据或运算符

            self.v.set('0')

            self.v1.set('0')


    # 清空操作  (清空用户输入的所有数据)
    def clear(self):

        self.lists = []
        self.v.set('0')
        self.v1.set('0')
        self.bj = False

    # 正负操作
    def fan(self):
        strnum = self.v.get()
        if strnum[0] == '-':
            self.v.set(strnum[1:])
            self.v1.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.v.set('-' + strnum)
            self.v1.set('-' + strnum)

    # 百分号
    def baifen(self):
        if self.v.get() !=0: #检测输入的数是否为0
            result = (int(self.v.get())/100)
            self.v.set(result)
            self.v1.set(result)

    # 平方
    def pingfang(self):
       result =int( self.v.get())**2 #平方运算
       self.v.set(result)
       self.v1.set(result)

    #开平方
    def sqrt(self):
        result = math.sqrt(int(self.v.get())) #运用数学模块完成开平方
        self.v.set(result)
        self.v1.set(result)

    #分数
    def fenshu(self):

        if self.v.get() != '0': #判断被除数不能为0
            result = 1/int(self.v.get())
            self.v.set(result)
            self.v1.set(result)



    # 等于号被按下的函数
    def deng(self):
        try:

            self.lists.append(self.v.get()) #把输入的数据和原先输出的数据拼接到一起
            str1 = ''.join(self.lists) # 将结果转化为字符窜形式
            result = eval(str1) # 将字符转化为pathon代码 进行运算
            self.v.set(result)
            self.v1.set(result)
            self.lists.clear() #运算完之后清空列表
        except ZeroDivisionError:  # 除数不能为零
            self.v.set('除数不能为零')



    def showlabel (self):

        def hello(self):
            print('帮助文档')
        # 创建总菜单
        menubar = tkinter.Menu(self.root)
        # 创建一个下拉菜单，并且加入文件菜单
        filemenu = tkinter.Menu(menubar)
        # 创建下来菜单的选项
        filemenu.add_command(label="about", command=hello)
        # 创建下拉菜单的分割线
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        # 将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
        menubar.add_cascade(label="File", menu=filemenu)

        # 显示总菜单
        self.root.config(menu=menubar)


        # 顶部区域
        self.v = tkinter.StringVar()
        self.v.set('0')
        self.v1 = tkinter.StringVar()
        self.v1.set('0')

        # 显示面板
        label = tkinter.Label(self.root, bg='white', textvariable=self.v, font=('黑体', 30), width=15, anchor='e',
                              borderwidth=10).place(x=0, y=20,width =367)
        #运算过程显示界面
        label1 = tkinter.Label(self.root, bg='white', textvariable=self.v1, font=('黑体', 13), width=15, anchor='e',borderwidth=10).place(x=0, y=0,width =367,height = 20)

        # 添加数字

        btn1 = tkinter.Button(self.root, text=1, font=('黑体', 15), command=lambda: self.num('1')).place(x=0, y=200.6, width=92,
                                                                                               height=59.7)
        btn2 = tkinter.Button(self.root, text=2,font=('黑体', 15), command=lambda: self.num('2')).place(x=92, y=200.6, width=92,
                                                                                               height=59.7)
        btn3 = tkinter.Button(self.root, text=3, font=('黑体', 15), command=lambda: self.num('3')).place(x=184, y=200.6, width=92,
                                                                                               height=59.7)

        btn4 = tkinter.Button(self.root, text=4, font=('黑体', 15), command=lambda: self.num('4')).place(x=0, y=260.4, width=92,
                                                                                               height=59.7)
        btn5 = tkinter.Button(self.root, text=5, font=('黑体', 15), command=lambda: self.num('5')).place(x=92, y=260.4, width=92,
                                                                                               height=59.7)
        btn6 = tkinter.Button(self.root, text=6, font=('黑体', 15), command=lambda: self.num('6')).place(x=184, y=260.4, width=92,
                                                                                               height=59.7)

        btn7 = tkinter.Button(self.root, text=7, font=('黑体', 15), command=lambda: self.num('7')).place(x=0, y=320.2, width=92,
                                                                                               height=59.7)
        btn8 = tkinter.Button(self.root, text=8, font=('黑体', 15), command=lambda: self.num('8')).place(x=92, y=320.2, width=92,
                                                                                               height=59.7)
        btn9 = tkinter.Button(self.root, text=9, font=('黑体', 15), command=lambda: self.num('9')).place(x=184, y=320.2, width=92,
                                                                                               height=59.7)
        btn0 = tkinter.Button(self.root, text=0, font=('黑体', 15), command=lambda:self. num('0')).place(x=0, y=380, width=92,
                                                                                               height=59.7)

        # 运算符
        jia = tkinter.Button(self.root, text='+', font=('黑体', 15), command=lambda: self.ys('+')).place(x=276, y=200.6,
                                                                                                width=92, height=59.7)
        jian = tkinter.Button(self.root, text='-', font=('黑体', 15), command=lambda: self.ys('-')).place(x=276, y=260.4,
                                                                                                 width=92, height=59.7)
        cheng = tkinter.Button(self.root, text='x', font=('黑体', 15), command=lambda: self.ys('*')).place(x=276, y=320.2,
                                                                                                  width=92, height=59.7)
        dian = tkinter.Button(self.root, text='.', font=('黑体', 15), command=lambda: self.num('.')).place(x=92, y=380,
                                                                                                 width=92, height=59.7)
        chu = tkinter.Button(self.root, text='/', font=('黑体', 15), command=lambda: self.ys('/')).place(x=184, y=380,
                                                                                                 width=92, height=59.7)
        deng1 = tkinter.Button(self.root, text='=', font=('黑体', 15), command=(self.deng)).place(x=276, y=380,
                                                                                                width=92, height=59.7)

        del1 = tkinter.Button(self.root, text='←', font=('黑体', 15), command=self.delete).place(x=0, y=140.8, width=92,
                                                                                                 height=59.7)
        clear = tkinter.Button(self.root, text='C', font=('黑体', 15), command=self.clear).place(x=92, y=140.8, width=92,
                                                                                                  height=59.7)
        fan = tkinter.Button(self.root, text='±', font=('黑体', 15), command=self.fan).place(x=184, y=140.8, width=92,
                                                                                                height=59.7)
        ce = tkinter.Button(self.root, text='CE', font=('黑体', 15), command=self.ce).place(x=276, y=140.8, width=92,
                                                                                                   height=59.7)

        baifen = tkinter.Button(self.root, text='%', font=('黑体', 15), command=self.baifen).place(x=0, y=81, width=92,
                                                                                                 height=59.7)

        pingfang = tkinter.Button(self.root, text='x²', font=('黑体', 15), command=self.pingfang).place(x=92, y=81,width=92,
                                                                                                 height=59.7)

        sqrt = tkinter.Button(self.root, text='√', font=('黑体', 15), command=self.sqrt).place(x=184, y=81, width=92,height=59.7)

        fenshu = tkinter.Button(self.root, text='1/x', font=('黑体', 15), command=self.fenshu).place(x=276, y=81, width=92,height=59.7)


        self.root.mainloop()


demo = Demo()












