

import random
import time
import tkinter
import threading


class Solo:

    bj = False# 标志符  为了确定结束键被按下
    bj1 =False# 标志符  为了确保开始按键 在第一次按下时才有效果
    bj2 = False # 标志符  只有按下开始键时,结束见按下才能起作用

    def __init__(self):

        self.root = tkinter.Tk()
        self.root.minsize(900, 600)
        self.root.title('solo大赛')
        self.showable()
        self.root.mainloop()

    #显示区域
    def showable(self):

        self.val = tkinter.StringVar()
        self.val.set('请选择需要\n solo的选手')  # 文本设置

        # 添加显示窗口

        # 标签  显示被选到的信息
        label1 = tkinter.Label(self.root, textvariable=self.val, bg='yellow', font=('黑体', 12), width='15', anchor='e',borderwidth='10')
        label1.place(x='385', y='50', width=130, height=60)

        self.pk = tkinter.Label(self.root, bg='yellow', text='V\nS', font=('黑体', 20))
        self.pk.place(x=420, y=240, width=60, height=120)

        # 添加成员
        self.chenglong = tkinter.Label(self.root, bg='pink', text='成龙')
        self.chenglong.place(x=50, y=275, width=50, height=50)

        self.lilianjie = tkinter.Label(self.root, bg='pink', text='李连杰')
        self.lilianjie.place(x=112.5, y=150, width=50, height=50)

        self.lixiaolong = tkinter.Label(self.root, bg='pink', text='李小龙')
        self.lixiaolong.place(x=187.5, y=50, width=50, height=50)

        self.wujing = tkinter.Label(self.root, bg='pink', text='吴京')
        self.wujing.place(x=112.5, y=400, width=50, height=50)

        self.zhangjin = tkinter.Label(self.root, bg='pink', text='张晋')
        self.zhangjin.place(x=262.5, y=150, width=50, height=50)

        self.zhaowenzuo = tkinter.Label(self.root, bg='pink', text='赵文卓')
        self.zhaowenzuo.place(x=325, y=275, width=50, height=50)

        self.yuanbiao = tkinter.Label(self.root, bg='pink', text='元彪')
        self.yuanbiao.place(x=262.5, y=400, width=50, height=50)

        self.yuanhua = tkinter.Label(self.root, bg='pink', text='元华')
        self.yuanhua.place(x=187.5, y=500, width=50, height=50)

        self. wusong = tkinter.Label(self.root, bg='pink', text='武松')
        self.wusong.place(x=526, y=275, width=50, height=50)

        self.linchong = tkinter.Label(self.root, bg='pink', text='林冲')
        self.linchong.place(x=588.5, y=150, width=50, height=50)

        self.caijin = tkinter.Label(self.root, bg='pink', text='柴进')
        self.caijin.place(x=663.5, y=50, width=50, height=50)

        self. yangzi = tkinter.Label(self.root, bg='pink', text='杨志')
        self.yangzi.place(x=588.5, y=400, width=50, height=50)

        self.wuyong = tkinter.Label(self.root, bg='pink', text='吴用')
        self.wuyong.place(x=738.5, y=150, width=50, height=50)

        self.songjiang = tkinter.Label(self.root, bg='pink', text='宋江')
        self.songjiang.place(x=801, y=275, width=50, height=50)

        self.guansheng = tkinter.Label(self.root, bg='pink', text='关胜')
        self.guansheng.place(x=738.5, y=400, width=50, height=50)

        self.huarong = tkinter.Label(self.root, bg='pink', text='花荣')
        self.huarong.place(x=663.5, y=500, width=50, height=50)




        # 添加开始结束键
        self.btn_start = tkinter.Button(self.root,bg ='red', text='开始', command=self.start)
        self.btn_start.place(x=340, y=500, width=80, height=80)

        self.btn_stop = tkinter.Button(self.root,bg ='blue', text='结束', command=self.stop)
        self.btn_stop.place(x=480, y=500, width=80, height=80)
        
    
        # 定义列表存放姓名

        self.list1 = [self.chenglong, self.lilianjie, self.lixiaolong, self.wujing, self.zhangjin, self.zhaowenzuo, self.yuanbiao,self. yuanhua]

        self.list2 = [self. wuyong, self.songjiang,self. guansheng, self.huarong,self.wusong, self.linchong,self. caijin, self.yangzi]

        self.max1_index = len(self.list1) - 1 #获得liset1的索引最大值
        self.max2_index = len(self.list2) - 1 #获得liset2的索引最大值
        # 起始索引
        self.start1_index = 0 #设置起始索引值为 0
        self.start2_index = 0



    # 定义一个开始的函数

    def start(self):

        if self.bj1 ==False: # 开始按键执行时  bj1 ==False

            # 开启一个线程来控制微循环
            self.t = threading.Thread(target=self.xunhuan)
            self.t.start()


        self.bj1 = True # 开始执行后 标识符 bj1 =True
        self.bj2 = True # 开始键被按下后, 使 bj2 =True

    def xunhuan(self):

        while True:
            # 判断是否按下结束
            if self.bj == True:  # 结束键已经按下
                self.bj = False
                return

            time.sleep(0.05)
            # 让所有的选项变成红色和蓝色
            for self.x in self.list1: #便利列表list1的所有元素
                self.x['bg'] = 'red'
            for self.y in self.list2:
                self.y['bg'] = 'blue'
            # 让当前的选项变成黄色
            self.list1[self.start1_index]['bg'] = 'yellow'
            self.list2[self.start2_index]['bg'] = 'yellow'
            #把随机选取出来的值链接起来并且输出
            self.val.set(self.list1[self.start1_index]['text'] +'VS'+self.list2[self.start2_index]['text'] )
            # 索引加一，准备下一个选项变红
            self.start1_index =random.randrange(0,11)

            self.start1_index += 1
            self.start2_index += 1
            # 判断索引值最大为列表的元素个数，如果大于元素个数让起始索引归零

            if self.start1_index > self.max1_index or self.start2_index > self.max2_index:
                self.start1_index = 0
                self.start2_index = 0

                # 定义一个结束的函数

    def stop(self):

        if self.bj2 ==True: # 开始按键被按下,可以按结束键

            self.bj1 = False  # 开始键被按下,并且只第一次被按下使有效果

            self.bj = True  # 结束键被按下



        self.bj2 = False #  结束键被按下,返回标识符(只有开始键被按下时,结束键才有效果)

solo = Solo()


























