import random
import time
import tkinter
import threading
class Dianming:

    bj=False
    bj1=False
    bj2=False
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.minsize(250,250)
        self.root.title('随机点名')
        self.showable()
        self.root.mainloop()

    #显示区域
    def showable(self):

        #添加姓名标签及开始结束按钮
        self.xiaonaoxu=tkinter.Label(self.root,bg='white',text='小挠许')
        self.xiaonaoxu.place(x=10,y=10,width=50,height=50)
        self.daxiji=tkinter.Label(self.root,bg='white',text='大西几')
        self.daxiji.place(x=70,y=10,width=50,height=50)
        self.xiaosongxu=tkinter.Label(self.root,bg='white',text='小松许')
        self.xiaosongxu.place(x=130,y=10,width=50,height=50)
        self.damangxie=tkinter.Label(self.root,bg='white',text='大蟒鞋')
        self.damangxie.place(x=190,y=10,width=50,height=50)
        self.danaofu=tkinter.Label(self.root,bg='white',text='大脑腐')
        self.danaofu.place(x=190,y=70,width=50,height=50)
        self.qiangjingnu=tkinter.Label(self.root,bg='white',text='墙颈怒')
        self.qiangjingnu.place(x=190,y=130,width=50,height=50)
        self.xiaobaiqu=tkinter.Label(self.root,bg='white',text='小白去')
        self.xiaobaiqu.place(x=190,y=190,width=50,height=50)
        self.dafeinang=tkinter.Label(self.root,bg='white',text='大飞馕')
        self.dafeinang.place(x=130,y=190,width=50,height=50)
        self.manyangyang=tkinter.Label(self.root,bg='white',text='慢羊羊')
        self.manyangyang.place(x=70,y=190,width=50,height=50)
        self.nuanyangyang=tkinter.Label(self.root,bg='white',text='暖羊羊')
        self.nuanyangyang.place(x=10,y=190,width=50,height=50)
        self.lanyangyang=tkinter.Label(self.root,bg='white',text='懒羊羊')
        self.lanyangyang.place(x=10,y=130,width=50,height=50)
        self.xiaohuihui=tkinter.Label(self.root,bg='white',text='小灰灰')
        self.xiaohuihui.place(x=10,y=70,width=50,height=50)
        self.btn_start = tkinter.Button(self.root, text='开始',command=self.start)
        self.btn_start.place(x=70, y=100, width=50, height=50)
        self.btn_end = tkinter.Button(self.root, text='结束',command=self.end)
        self.btn_end.place(x=130, y=100, width=50, height=50)
        self.lists=[self.xiaonaoxu,self.daxiji,self.xiaosongxu,self.damangxie,self.danaofu,self.qiangjingnu,self.xiaobaiqu,self.dafeinang,self.manyangyang,self.nuanyangyang,self.lanyangyang,self.xiaohuihui]



        #获取最大索引值
        self.max_index=len(self.lists)-1
        self.start_index=0#设置起始索引值
    #定义一个开始函数
    def start(self):
        if self.bj1==False:
            self.t=threading.Thread(target=self.xunhuan)
            self.t.start()

        self.bj1=True#开始执行后，标识符 bj1=True
        self.bj2=True#开始键按下后，使 bj2=True
    def xunhuan(self):
        while True:
            #判断是否按下结束
            if self.bj==True:#a结束键已经按下
                self.bj=False
                return
            time.sleep(0.05)
            for self.x in self.lists:
                self.x['bg']='red'
            #让当前的选项变成黄色
            self.lists[self.start_index]['bg']='yellow'

            #索引加一，准备下一个选项变红
            self.start_index=random.randrange(0,12)
            self.start_index+=1
            #判断索引值最大为列表的元素的个数，如果大于元素个数让起始索引归为0
            if self.start_index>self.max_index:
                self.start_index=0
    #定义一个结束的函数
    def end(self):
        if self.bj2==True:#开始键被按下，可以按结束建
            self.bj1=False#开始键被按下，并且只第一次被按下有结果
            self.bj=True#结束键被按下
        self.bj2=False#结束键被按下，返回标识符（只有开始键被按下时，结束建才有效果）
dianming=Dianming()